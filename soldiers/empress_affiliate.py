#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import requests
import datetime
import time
import schedule

# -------------------------------
# Load Secrets
# -------------------------------
load_dotenv('secrets.env')
AFFILIATE_ID = os.getenv("AFFILIATE_ID")

# -------------------------------
# EMPRESS Narration Protocol
# -------------------------------
def empress_narrate(message):
    timestamp = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[EMPRESS] {timestamp} — {message}")
    with open("affiliate.log", "a") as log:
        log.write(f"[EMPRESS] {timestamp} — {message}\n")

# -------------------------------
# EMPRESS Affiliate Scan
# -------------------------------
def empress_scan_affiliates():
    empress_narrate("Scanning affiliate feeds...")
    try:
        response = requests.get(f"https://api.affiliatenetwork.com/promos?affiliate_id={AFFILIATE_ID}")
        if response.status_code == 200:
            promos = response.json().get("promotions", [])
            for promo in promos:
                title = promo.get("title", "Untitled")
                reward = promo.get("reward", "Unknown")
                link = promo.get("link", "")
                empress_narrate(f"Promo: {title} — Reward: {reward} — {link}")
        else:
            empress_narrate(f"Affiliate scan failed: {response.status_code}")
    except Exception as e:
        empress_narrate(f"Affiliate scan error: {str(e)}")

# -------------------------------
# EMPRESS Mutation Loop
# -------------------------------
def empress_mutate():
    empress_narrate("EMPRESS affiliate mutation initiated.")
    empress_scan_affiliates()
    empress_narrate("EMPRESS affiliate mutation completed.")

# -------------------------------
# EMPRESS Scheduler: Every 3 Hours
# -------------------------------
schedule.every(3).hours.do(empress_mutate)

# -------------------------------
# EMPRESS Execution Loop
# -------------------------------
empress_narrate("EMPRESS affiliate soldier deployed. Awaiting mutation cycles...")
while True:
    schedule.run_pending()
    time.sleep(60)
