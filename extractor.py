import requests
from bs4 import BeautifulSoup
import re

def extract_single_lead(res):
    url = res['url']
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()
        emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+", text)))
    except:
        emails = []
    return {
        'Title': res['title'],
        'URL': res['url'],
        'Snippet': res['snippet'],
        'Emails': ", ".join(emails[:3]) if emails else 'Not Found'
    }