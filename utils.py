from stem import Signal
from stem.control import Controller
import requests

def renew_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_password')
            controller.signal(Signal.NEWNYM)
    except Exception as e:
        print("Failed to renew Tor IP:", e)

def get_current_ip():
    try:
        ip = requests.get('http://httpbin.org/ip', proxies={
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }, timeout=10).json()
        return ip.get("origin")
    except:
        return "Unable to fetch IP"
