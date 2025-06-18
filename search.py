from duckduckgo_search import DDGS
from utils import renew_tor_ip
import time

def perform_search(query, location, include_keywords, exclude_keywords, max_results, retries=3):
    email_modifiers = ["contact", "email", "reach us", "get in touch", "@"]
    final_query = query + " " + " ".join(email_modifiers)

    if location:
        final_query += f" in {location}"
    if include_keywords:
        final_query += " " + " ".join(include_keywords.split(","))
    if exclude_keywords:
        for word in exclude_keywords.split(","):
            final_query += f" -{word.strip()}"

    for attempt in range(retries):
        try:
            results = []
            with DDGS(proxies={"http": "socks5h://127.0.0.1:9050",
                               "https": "socks5h://127.0.0.1:9050"}) as ddgs:
                for r in ddgs.text(final_query, max_results=max_results):
                    results.append({
                        'title': r.get('title'),
                        'url': r.get('href'),
                        'snippet': r.get('body')
                    })
            return results  # Success
        except Exception as e:
            print(f"[Attempt {attempt+1}/{retries}] Search error: {e}")
            print("🔄 Renewing Tor IP and retrying...")
            renew_tor_ip()
            time.sleep(7)  # Allow new Tor circuit to initialize

    # All retries failed
    print("❌ All retries failed. Aborting search.")
    return []
