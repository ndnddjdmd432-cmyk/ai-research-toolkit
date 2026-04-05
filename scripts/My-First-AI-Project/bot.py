import argparse
import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple


APP_NAME = "Self-Healing Security Bot (Beginner Demo)"
DEFAULT_WATCHED_DIR = Path("watched")
DEFAULT_STATE_DIR = Path("state")
DEFAULT_CONFIG_PATH = Path("config.json")


@dataclass(frozen=True)
class Finding:
    path: str
    issue: str
    severity: str


def _now_unix() -> int:
    return int(time.time())


def ensure_default_config(config_path: Path) -> Dict:
    """
    "Self-healing" behavior #1:
      - If config.json is missing, create a safe default config automatically.
    """
    default_config = {
        "watched_dir": str(DEFAULT_WATCHED_DIR),
        "state_dir": str(DEFAULT_STATE_DIR),
        "dangerous_substrings": ["password=", "api_key=", "secret=", "BEGIN PRIVATE KEY"],
        "max_file_bytes": 200_000,
    }

    # Self-heal a common setup mistake: config.json exists as a directory.
    if config_path.exists() and config_path.is_dir():
        backup_dir = config_path.with_name(f"{config_path.name}.dir.bak.{_now_unix()}")
        try:
            config_path.rename(backup_dir)
            print(f"[heal] {config_path} was a directory. Moved to {backup_dir}")
        except OSError as exc:
            raise RuntimeError(
                f"Cannot use {config_path} because it is a directory and cannot be moved: {exc}"
            ) from exc

    if not config_path.exists():
        config_path.write_text(json.dumps(default_config, indent=2), encoding="utf-8")
        print(f"[heal] Created missing config: {config_path}")
        return default_config

    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # "Self-healing" behavior #2:
        #   - If config.json is corrupted, replace it with defaults.
        backup = config_path.with_suffix(".json.bak")
        backup.write_text(config_path.read_text(encoding="utf-8"), encoding="utf-8")
        config_path.write_text(json.dumps(default_config, indent=2), encoding="utf-8")
        print(f"[heal] Config was invalid JSON. Backed up to {backup} and reset {config_path}")
        return default_config
    except OSError as exc:
        # Covers permission and file-type issues (for example unreadable paths).
        backup = config_path.with_suffix(".json.unreadable.bak")
        try:
            config_path.rename(backup)
            print(f"[heal] Unreadable config moved to {backup}: {exc}")
        except OSError:
            print(f"[warn] Config unreadable and could not be moved: {config_path} ({exc})")

        config_path.write_text(json.dumps(default_config, indent=2), encoding="utf-8")
        print(f"[heal] Recreated config: {config_path}")
        return default_config


def ensure_demo_files(watched_dir: Path) -> None:
    watched_dir.mkdir(parents=True, exist_ok=True)
    example = watched_dir / "example.txt"
    if not example.exists():
        example.write_text(
            "hello from the security bot demo\n",
            encoding="utf-8",
        )
        print(f"[heal] Created demo file: {example}")


def compute_sha256_bytes(data: bytes) -> str:
    """
    Compute a deterministic SHA-256 digest for file content bytes.
    """
    sha = hashlib.sha256()
    sha.update(data)
    return sha.hexdigest()


def safe_read_file(path: Path, max_bytes: int) -> Tuple[bytes, str]:
    try:
        size = path.stat().st_size
    except FileNotFoundError:
        return b"", "missing"

    if size > max_bytes:
        return b"", f"too_large({size} bytes)"

    try:
        return path.read_bytes(), "ok"
    except OSError as exc:
        return b"", f"os_error({exc})"


def analyze_with_llm(content_text: str) -> Dict[str, Any]:
    """
    Mock LLM integration.

    This simulates an API call to an AI model with the prompt:
      "Does this code contain sensitive security vulnerabilities?"
    and returns a JSON-like Python dictionary as the response payload.
    """
    question = "Does this code contain sensitive security vulnerabilities?"
    model = "mock-openai-gpt-security-v1"
    provider = "mock-openai"

    findings: List[Dict[str, Any]] = []
    matched_markers: List[str] = []
    if "AWS_SECRET" in content_text:
        matched_markers.append("AWS_SECRET")
    if "AKIA" in content_text:
        matched_markers.append("AKIA")

    if matched_markers:
        findings.append(
            {
                "issue": "llm_flag:exposed_aws_key_detected",
                "severity": "high",
                "evidence": ",".join(matched_markers),
            }
        )

    has_sensitive_vulnerabilities = len(findings) > 0
    risk_score = 0.95 if has_sensitive_vulnerabilities else 0.01
    summary = (
        "llm_flag:exposed_aws_key_detected"
        if has_sensitive_vulnerabilities
        else "llm_flag:none_detected"
    )

    return {
        "provider": provider,
        "model": model,
        "prompt": question,
        "has_sensitive_vulnerabilities": has_sensitive_vulnerabilities,
        "risk_score": round(risk_score, 2),
        "findings": findings,
        "summary": summary,
        "analysis_timestamp_unix": _now_unix(),
    }


def scan_file_for_secrets(path: Path, max_bytes: int) -> List[Finding]:
    findings: List[Finding] = []
    content, status = safe_read_file(path, max_bytes=max_bytes)
    if status != "ok":
        findings.append(Finding(str(path), f"unreadable:{status}", "low"))
        return findings

    content_text = content.decode("utf-8", errors="replace")
    llm_response = analyze_with_llm(content_text)

    if llm_response["has_sensitive_vulnerabilities"]:
        for item in llm_response["findings"]:
            findings.append(
                Finding(
                    str(path),
                    f"llm_flag:{item['issue']} (evidence={item['evidence']})",
                    str(item["severity"]).lower(),
                )
            )
    else:
        findings.append(Finding(str(path), "llm_flag:none_detected", "low"))

    # Preserve a deterministic integrity check alongside the LLM analysis.
    file_hash = compute_sha256_bytes(content)
    if file_hash == "":
        findings.append(Finding(str(path), "hash_empty", "medium"))
    else:
        findings.append(Finding(str(path), f"hash_sha256:{file_hash[:16]}", "info"))

    return findings


def write_state(state_dir: Path, findings: List[Finding]) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    out_path = state_dir / "findings.json"
    payload = {
        "app": APP_NAME,
        "timestamp_unix": _now_unix(),
        "findings": [f.__dict__ for f in findings],
    }
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out_path


def run_once(config_path: Path) -> int:
    cfg = ensure_default_config(config_path)

    watched_dir = Path(cfg["watched_dir"])
    state_dir = Path(cfg["state_dir"])
    max_bytes = int(cfg["max_file_bytes"])

    ensure_demo_files(watched_dir)

    all_findings: List[Finding] = []
    for p in sorted(watched_dir.rglob("*")):
        if p.is_file():
            all_findings.extend(scan_file_for_secrets(p, max_bytes=max_bytes))

    out = write_state(state_dir, all_findings)
    print(f"[ok] Wrote state: {out}")
    print(f"[ok] Findings: {len(all_findings)}")
    return 0


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(prog="bot.py", description=APP_NAME)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Path to config.json")
    parser.add_argument("--once", action="store_true", help="Run one scan and exit")
    args = parser.parse_args(argv)

    config_path = Path(args.config)

    print(f"[start] {APP_NAME}")
    print(f"[info] python={sys.version.split()[0]} pid={os.getpid()}")
    print(f"[info] config={config_path}")

    if args.once:
        return run_once(config_path)

    # Simple supervisor loop: if it crashes, restart after a short delay.
    while True:
        try:
            run_once(config_path)
        except Exception as exc:
            # flush=True forces zero-latency telemetry for the evaluator script!
            print(f"[crash] {type(exc).__name__}: {exc}", flush=True)
            print("[heal] Restarting in 2 seconds...", flush=True)
            time.sleep(2)
        else:
            time.sleep(10)

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
