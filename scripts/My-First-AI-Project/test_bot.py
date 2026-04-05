import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Dict, List, Optional


ANSI_GREEN = "\033[92m"
ANSI_RED = "\033[91m"
ANSI_RESET = "\033[0m"


def _print_header(title: str) -> None:
    bar = "=" * len(title)
    print(bar)
    print(title)
    print(bar)


def _print_banner_success() -> None:
    banner = [
        "############################################################",
        "#                                                          #",
        "#   SHOWCASE EVALUATION PASSED: BOT HEALED ITSELF         #",
        "#                                                          #",
        "############################################################",
    ]
    print(f"{ANSI_GREEN}")
    for line in banner:
        print(line)
    print(ANSI_RESET, end="")


def _print_banner_failure(reason: str) -> None:
    print(f"{ANSI_RED}SHOWCASE EVALUATION FAILED{ANSI_RESET}: {reason}")


def _copy_bot_script(source_root: Path, temp_root: Path) -> Path:
    src = source_root / "bot.py"
    if not src.exists():
        raise FileNotFoundError(f"Cannot find bot.py at {src}")
    dst = temp_root / "bot.py"
    shutil.copy2(src, dst)
    return dst


def _create_corrupted_workspace(temp_root: Path) -> Path:
    watched = temp_root / "watched"
    state = temp_root / "state"
    watched.mkdir(parents=True, exist_ok=True)
    state.mkdir(parents=True, exist_ok=True)
    (watched / "example.txt").write_text("password=demo_secret_value\n", encoding="utf-8")

    config_dir = temp_root / "config.json"
    config_dir.mkdir(parents=True, exist_ok=True)
    lock_path = config_dir / "lockfile.tmp"
    lock_path.write_text("lock me", encoding="utf-8")
    return lock_path


def _launch_bot(temp_root: Path) -> subprocess.Popen:
    cmd = [sys.executable, "bot.py"]
    return subprocess.Popen(
        cmd,
        cwd=str(temp_root),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )


def _classify_line(line: str) -> Dict[str, bool]:
    return {
        "is_crash": "[crash]" in line,
        "is_heal": "[heal]" in line,
        "is_heal_restart": "[heal] Restarting" in line,
        "is_heal_dir": "was a directory" in line,
        "is_heal_created": "Created missing config" in line,
        "is_ok": "[ok] Wrote state:" in line,
    }


def _evaluate_sequence(events: List[Dict[str, object]]) -> Dict[str, object]:
    crash_indices = [i for i, e in enumerate(events) if e["is_crash"]]
    heal_indices = [i for i, e in enumerate(events) if e["is_heal"]]
    restart_indices = [i for i, e in enumerate(events) if e["is_heal_restart"]]
    dir_heal_indices = [i for i, e in enumerate(events) if e["is_heal_dir"]]
    created_indices = [i for i, e in enumerate(events) if e["is_heal_created"]]
    ok_indices = [i for i, e in enumerate(events) if e["is_ok"]]

    # Mathematical checks:
    # 1) Crash must happen at least once.
    # 2) Heal must happen at least once.
    # 3) Recovery signal [ok] must happen after crash+heal.
    # 4) Workspace corruption must be addressed by directory-heal or config recreation.
    has_crash = len(crash_indices) >= 1
    has_heal = len(heal_indices) >= 1
    has_restart = len(restart_indices) >= 1
    has_ok = len(ok_indices) >= 1
    has_config_repair = len(dir_heal_indices) >= 1 or len(created_indices) >= 1

    order_valid = False
    if has_crash and has_heal and has_ok:
        first_crash = crash_indices[0]
        first_heal_after_crash = next((i for i in heal_indices if i > first_crash), None)
        first_ok_after_heal = None
        if first_heal_after_crash is not None:
            first_ok_after_heal = next((i for i in ok_indices if i > first_heal_after_crash), None)
        order_valid = first_heal_after_crash is not None and first_ok_after_heal is not None

    score = int(has_crash) + int(has_heal) + int(has_restart) + int(has_ok) + int(has_config_repair) + int(order_valid)
    passed = all([has_crash, has_heal, has_ok, has_config_repair, order_valid])

    return {
        "passed": passed,
        "score": score,
        "max_score": 6,
        "has_crash": has_crash,
        "has_heal": has_heal,
        "has_restart": has_restart,
        "has_ok": has_ok,
        "has_config_repair": has_config_repair,
        "order_valid": order_valid,
    }


def run_stress_test(timeout_seconds: int = 45) -> int:
    source_root = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(prefix="bot_stress_eval_") as tmp:
        temp_root = Path(tmp)
        _copy_bot_script(source_root, temp_root)
        lock_path = _create_corrupted_workspace(temp_root)

        # Keep file handle open so config directory rename can fail on first attempt (PermissionError).
        lock_handle = open(lock_path, "r", encoding="utf-8")

        _print_header("Stress Test: Self-Healing Architecture Evaluation")
        print(f"Workspace: {temp_root}")
        print(f"Interpreter: {sys.executable}")
        print("Corruption injected: directory named config.json + active lock handle")
        print("-" * 60)

        proc = _launch_bot(temp_root)
        events: List[Dict[str, object]] = []

        crashed_and_restarting = False
        lock_released = False
        start_time = time.time()

        try:
            assert proc.stdout is not None
            while time.time() - start_time < timeout_seconds:
                line = proc.stdout.readline()
                if line == "" and proc.poll() is not None:
                    break
                if not line:
                    time.sleep(0.05)
                    continue

                stripped = line.rstrip("\n")
                print(stripped)
                flags = _classify_line(stripped)
                event = {"line": stripped, **flags}
                events.append(event)

                if flags["is_crash"] or flags["is_heal_restart"]:
                    crashed_and_restarting = True

                # Release the lock after we observe a crash+restart signal so the next cycle can heal and recover.
                if crashed_and_restarting and (not lock_released):
                    lock_handle.close()
                    lock_released = True
                    print("[tester] Released lock handle to allow self-healing recovery path.")

                if flags["is_ok"]:
                    break
        finally:
            if not lock_handle.closed:
                lock_handle.close()
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()

        print("-" * 60)
        summary = _evaluate_sequence(events)
        print(
            "Score: "
            f"{summary['score']}/{summary['max_score']} | "
            f"crash={summary['has_crash']} heal={summary['has_heal']} "
            f"restart={summary['has_restart']} ok={summary['has_ok']} "
            f"config_repair={summary['has_config_repair']} order={summary['order_valid']}"
        )

        if summary["passed"]:
            _print_banner_success()
            return 0

        _print_banner_failure("Expected crash -> heal -> recovery sequence not fully observed.")
        return 1


if __name__ == "__main__":
    raise SystemExit(run_stress_test())
