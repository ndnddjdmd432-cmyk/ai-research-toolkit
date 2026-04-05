import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError
import logging
from config import GEMINI_API_KEY

# Configure the Gemini API key securely
genai.configure(api_key=GEMINI_API_KEY)

# The strict rules from your blueprint
SYSTEM_INSTRUCTION = """You are an AI news analyst. I will give you the title and raw text
from a blog post or research paper abstract. You must return a
response in STRICTLY this format and no other format:

🚨 [CLASSIFICATION: Product Release / Research Paper / Rumor / Industry News]
📰 Headline: [Create a punchy, catchy headline in 5–7 words]
🧠 The TLDR: [Exactly 2 sentences. Sentence 1: what happened. Sentence 2: why it matters to the AI industry.]
🔗 Source: [Insert the URL provided]

STRICT RULES:
1. If the content is not related to AI, machine learning, or large
   language models, return only the single word: SKIP
2. Do not add any text, preamble, or explanation outside the format.
3. Do not use markdown bold or italic formatting.
4. The TLDR must be exactly 2 sentences — no more, no less."""

def summarize_article(title: str, raw_text: str, url: str) -> str:
    """Sends article data to Gemini 1.5 Flash and returns a formatted summary or None if skipped/failed."""
    
    # Construct the exact user prompt
    user_prompt = f"""
Title: {title}

Text: {raw_text}

URL: {url}
"""
    
    try:
        # Initialize the fast, cost-efficient model
        model = genai.GenerativeModel(
            model_name="models/gemini-3-flash-preview",
            system_instruction=SYSTEM_INSTRUCTION
        )
        
        # Call the Gemini API
        response = model.generate_content(user_prompt)
        
        # 1. Strip leading/trailing whitespace
        result_text = response.text.strip()
        
        # 2. If the response equals "SKIP" (case-insensitive) -> return None
        if result_text.upper() == "SKIP":
            return None
            
        # 3. If the response starts with "🚨" -> return the full response string to be sent to Telegram
        if result_text.startswith("🚨"):
            return result_text
            
        # 4. If the response is anything else unexpected -> log a warning and return None
        logging.warning(f"Unexpected Gemini response format for URL {url}. Response: {result_text}")
        return None
        
    except GoogleAPIError as e:
        logging.error(f"Gemini API Error for URL {url}: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error in summarizer for URL {url}: {e}")
        return None