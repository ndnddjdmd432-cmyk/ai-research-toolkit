import feedparser
import logging
import requests
from requests.exceptions import RequestException

def fetch_rss_feeds(feeds: list) -> list:
    """Fetches and parses all RSS feeds, returning a list of raw article dictionaries."""
    all_articles = []
    
    for feed in feeds:
        feed_name = feed.get("name", "Unknown Feed")
        feed_url = feed.get("url", "")
        
        logging.info(f"Fetching feed: {feed_name}")
        
        try:
            # We use a User-Agent so websites don't block us thinking we are a malicious bot
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AI-News-Scout/1.0'}
            response = requests.get(feed_url, headers=headers, timeout=10)
            response.raise_for_status() 
            
            # Parse the downloaded XML text using feedparser
            parsed_feed = feedparser.parse(response.content)
            
            for entry in parsed_feed.entries:
                article = {
                    "source": feed_name,
                    "title": getattr(entry, 'title', 'No Title'),
                    "link": getattr(entry, 'link', ''),
                    "summary": getattr(entry, 'summary', getattr(entry, 'description', 'No summary available.'))
                }
                
                # Only add the article if it actually has a valid URL
                if article["link"]:
                    all_articles.append(article)
                    
        except RequestException as e:
            logging.error(f"Network error fetching {feed_name}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error parsing {feed_name}: {e}")
            
    logging.info(f"Total articles fetched across all feeds: {len(all_articles)}")
    return all_articles