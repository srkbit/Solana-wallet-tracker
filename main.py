import os
import requests
import telebot
import time

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

# List of Solana wallet addresses to track
WALLETS = [
    "YOUR_FIRST_WALLET_ADDRESS",
    "YOUR_SECOND_WALLET_ADDRESS"
]

def check_wallet_activity(wallet):
    url = f"https://api.solscan.io/account/tokens?address={wallet}&limit=10"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers).json()
        # You can add logic here to detect specific token buys / tx
        bot.send_message(CHAT_ID, f"Checked wallet: {wallet}\nToken count: {len(response)}")
    except Exception as e:
        bot.send_message(CHAT_ID, f"Error checking {wallet}:\n{str(e)}")

if __name__ == "__main__":
    while True:
        for wallet in WALLETS:
            check_wallet_activity(wallet)
        time.sleep(60)
