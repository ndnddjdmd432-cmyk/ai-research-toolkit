import logging
import time
from config import RSS_FEEDS
from fetcher import fetch_rss_feeds
from summarizer import summarize_article
from notifier import send_telegram_message
from database import is_article_seen, mark_article_seen, init_db

# Setup logging to see the "heartbeat" of the program
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    print("🚀 Sentry is starting up...")
    logging.info("=== WAKING UP: Checking for AI News ===")
    
    # STEP 1: Initialize Database
    init_db()
    
    # STEP 2: Fetch articles using the list from config.py
    articles = fetch_rss_feeds(RSS_FEEDS)
    logging.info(f"Fetched {len(articles)} articles. Checking for new ones...")

    new_count = 0
    for article in articles:
        url = article.get('link')
        
        # STEP 3: Basic Validation
        if not url:
            continue

        # STEP 4: Duplicate Check (Memory)
        if is_article_seen(url):
            continue

        new_count += 1
        logging.info(f"Processing: {article.get('title')[:60]}...")

        # STEP 5: Summarize via Gemini API
        summary = summarize_article(
            title=article.get('title', ''),
            raw_text=article.get('summary', ''),
            url=url
        )
        
        # --- THE SPEED LIMIT FIX ---
        # We wait 4 seconds after every Gemini request to avoid the 429 Quota Error.
        # This keeps us under the "20 requests per minute" limit.
        time.sleep(4) 

        # STEP 6: Send Telegram & Save Memory (The Smart Logic)
        if summary and summary != "SKIP":
            # Only save the article as "seen" if it actually reached your phone!
            if send_telegram_message(summary):
                mark_article_seen(url)
                logging.info("✅ Sent to Telegram and saved to memory.")
            else:
                logging.error(f"❌ Telegram failed for {url}. Check your CHAT_ID.")
        
        elif summary == "SKIP":
            # If Gemini says it's not AI news, mark it seen so it doesn't check it again
            mark_article_seen(url)
            logging.info("⏭️ Skipped (Not relevant AI news).")

        else:
            # STEP 7: Quota/Error Management
            # If Gemini hits a 429 limit despite the sleep, we STOP to reset.
            logging.warning("⚠️ Gemini Quota hit or API Error. Stopping run to wait for reset.")
            break 

    logging.info(f"=== FINISHED: Processed {new_count} new articles. ===")

if __name__ == "__main__":
    main()