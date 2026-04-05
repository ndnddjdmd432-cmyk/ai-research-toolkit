import requests
import logging
from config import TELEGRAM_BOT_TOKEN, CHAT_ID

def send_telegram_message(message: str) -> bool:
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        # Check if Telegram actually said "OK"
        if response.status_code == 200:
            return True
        else:
            # If it's not 200, Telegram rejected it (bad ID or bad Token)
            logging.error(f"Telegram rejected message: {response.text}")
            return False
    except Exception as e:
        logging.error(f"Connection error to Telegram: {e}")
        return False