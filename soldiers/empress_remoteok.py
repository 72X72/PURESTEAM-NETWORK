#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import requests
import json
import datetime
import time
import schedule

# -------------------------------
# Load Secrets
# -------------------------------
load_dotenv('secrets.env')

# -------------------------------
# EMPRESS Narration Protocol
# -------------------------------
def empress_narrate(message):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[EMPRESS] {timestamp} — {message}")
    with open("income.log", "a") as log:
        log.write(f"[EMPRESS] {timestamp} — {message}\n")

# -------------------------------
# EMPRESS Income Scan: RemoteOK
# -------------------------------
def empress_scan_remoteok():
    empress_narrate("Scanning RemoteOK for monetizable gigs...")
    try:
        response = requests.get("https://remoteok.com/api")
        if response.status_code == 200:
            jobs = response.json()[1:]  # Skip metadata
            for job in jobs:
                title = job.get("position", "Untitled")
                company = job.get("company", "Unknown")
                url = job.get("url", "")
                empress_narrate(f"Found: {title} at {company} — {url}")
        else:
            empress_narrate(f"RemoteOK scan failed: {response.status_code}")
    except Exception as e:
        empress_narrate(f"RemoteOK scan error: {str(e)}")

# -------------------------------
# EMPRESS Mutation Loop
# -------------------------------
def empress_mutate():
    empress_narrate("EMPRESS income mutation initiated.")
    empress_scan_remoteok()
    empress_narrate("EMPRESS income mutation completed.")

# -------------------------------
# EMPRESS Scheduler: Every 3 Hours
# -------------------------------
schedule.every(3).hours.do(empress_mutate)

# -------------------------------
# EMPRESS Execution Loop
# -------------------------------
empress_narrate("EMPRESS soldier deployed. Awaiting mutation cycles...")
while True:
    schedule.run_pending()
    time.sleep(60)

