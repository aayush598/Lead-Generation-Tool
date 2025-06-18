import json
import os
from datetime import datetime

HISTORY_FILE = "data/leads_history.json"

def save_to_history(new_leads):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    else:
        history = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for lead in new_leads:
        lead['timestamp'] = timestamp
        history.append(lead)
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []