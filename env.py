import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "16039780").strip()
API_HASH = os.getenv("API_HASH", "43c5751eb09007121dcb3ee256213dc9").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5929113911:AAHFCGsl-QG0t40jOv0Pd_8OniZDQzNgEVs").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://kvdwzziy:DpoiBw49O3c24I_Ipvby9HcNeawU8nsX@tiny.db.elephantsql.com/kvdwzziy").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "@Jombloday")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
