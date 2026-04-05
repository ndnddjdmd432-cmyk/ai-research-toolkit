# ================================================================
# config.py — All credentials and configuration for the aggregator
# Fill in the placeholder values before running the script.
# ================================================================

# --- GEMINI API ---
# Get your key from: https://aistudio.google.com/app/apikey
GEMINI_API_KEY = "AIzaSyC8WixKbhnnooxrycFbop1I8oETBW3uH44"

# --- TELEGRAM BOT ---
# Step 1: Message @BotFather on Telegram, create a new bot, copy the token below.
# Step 2: Start a chat with your new bot, then visit:
#         https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
#         to find your personal Chat ID.
TELEGRAM_BOT_TOKEN = "8655465660:AAEe2uSquL2EvQV_-rpVgDCpd1wraqdA534"
CHAT_ID   = "7372107355"

# --- DATABASE ---
# Path to the SQLite file used for duplicate checking.
# os.path.join ensures this works on both Windows and Linux/cloud.
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "seen_articles.db")

# --- LOGGING ---
LOG_PATH = os.path.join(os.path.dirname(__file__), "aggregator.log")

# --- RSS FEEDS ---
# Add or remove feed dicts here to change what sources are monitored.
RSS_FEEDS = [
    {
        "name": "Hugging Face Blog",
        "url": "https://huggingface.co/blog/feed.xml"
    },
    {
        "name": "ArXiv CS.AI",
        "url": "http://export.arxiv.org/rss/cs.AI"
    },
    {
        "name": "OpenAI Research Blog",
        "url": "https://openai.com/blog/rss.xml"
    },
]