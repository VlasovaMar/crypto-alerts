import json
import requests
from datetime import datetime

# Load thresholds from config
with open("../configs/alert_config.json") as f:
    config = json.load(f)

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    return requests.get(url).json()[symbol]['usd']

def check_alerts():
    for coin, threshold in config.items():
        price = get_price(coin)
        if price >= threshold:
            msg = f"{datetime.now()}: {coin.upper()} crossed ${threshold}, current: ${price}"
            print(msg)
            with open("../examples/sample_alerts.log", "a") as log_file:
                log_file.write(msg + "\n")

if __name__ == "__main__":
    check_alerts()
