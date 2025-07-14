from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        for event in data.get("events", []):
            tx = event.get("description", {}).get("summary", "Unknown")
            wallet = event.get("account", "Unknown")
            send_telegram(f"🚨 Activity Detected\nWallet: {wallet}\nAction: {tx}")
    except Exception as e:
        send_telegram(f"Error: {str(e)}")
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
