#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# -------------------------------
# EMPRESS Injector Config
# -------------------------------
AFFILIATE_ID_RAW = "EMPRESS72"
WALLET_ADDRESS_RAW = "LIBERTY_CLOUD"

# -------------------------------
# Load or Generate Mutation Key
# -------------------------------
load_dotenv('secrets.env')
key = os.getenv("MUTATION_KEY")
if not key:
    key = Fernet.generate_key().decode()
    print("[EMPRESS INJECTOR] No key found. Generated new MUTATION_KEY.")

cipher = Fernet(key.encode())

# -------------------------------
# Encrypt Payloads
# -------------------------------
encrypted_affiliate = cipher.encrypt(AFFILIATE_ID_RAW.encode()).decode()
encrypted_wallet = cipher.encrypt(WALLET_ADDRESS_RAW.encode()).decode()

# -------------------------------
# Inject into secrets.env
# -------------------------------
with open("secrets.env", "w") as f:
    f.write(f"MUTATION_KEY={key}\n")
    f.write(f"AFFILIATE_ID_ENCRYPTED={encrypted_affiliate}\n")
    f.write(f"WALLET_ADDRESS_ENCRYPTED={encrypted_wallet}\n")

print("[EMPRESS INJECTOR] Payloads encrypted and injected.")
