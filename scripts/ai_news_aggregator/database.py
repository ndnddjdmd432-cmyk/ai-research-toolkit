import sqlite3
import logging
from config import DB_PATH

def init_db():
    """Initializes the SQLite database and creates the table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Create a table to store URLs we have already sent to Telegram
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS seen_articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        logging.info("Database initialized successfully.")
    except Exception as e:
        logging.error(f"Failed to initialize database: {e}")

def is_article_seen(url: str) -> bool:
    """Checks if a URL is already in the database. Returns True if seen, False if new."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM seen_articles WHERE url = ?", (url,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except Exception as e:
        logging.error(f"Database read error for URL {url}: {e}")
        # If the database breaks, assume we HAVE seen it so we don't spam your phone
        return True 

def mark_article_seen(url: str):
    """Saves a new URL into the database so it is never sent again."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO seen_articles (url) VALUES (?)", (url,))
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"Database write error for URL {url}: {e}")