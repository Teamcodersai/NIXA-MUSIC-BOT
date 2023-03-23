import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBztOc4zVywDsMvu_z1xmfU82NWfAvorlGuJOcKwahycTvuiS1r5TO8s9D7z8epzWaXrd1n8zKV4hKG6I3lp1KCY08gvXSp3Wc53WZjV81is01EuRZ_9sVQ5DgnNxRwGBhI_EriBH9pbttNEaYiWGKuBMYf8ufygtSSq45GYF5evo8V67DyQ0N38z3yohIxZl9CYU8pUH32lARl3iBlfM_kwVsa1l50pyy_-UHGU3SXnKB_pRalVeN8C0XI1952VKnxNaInoY7J5mEjrKytcoKgfGV1nAQBiDyc6BXHOvNxfWqkIcCJhCWbJhb9Kquu_OBE0goW9RKKyaHMAarWr0-qAAAAAWlv1vQA")
BOT_TOKEN = getenv("BOT_TOKEN", "6153257153:AAGGEFkNGwtHEMKLvj8Dx8EVbRkfPQ7YfPw")
BOT_NAME = getenv("BOT_NAME", "🆃ҽαɱ 🅲σԃҽɾ 🅼υʂιƈ")
API_ID = int(getenv("API_ID", "22875242"))
API_HASH = getenv("API_HASH", "32eddce639c6fd7fe6a40db879dcb91c")
OWNER_NAME = getenv("OWNER_NAME", "Samsari boltey")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Believe_Bad_Boy")
ALIVE_NAME = getenv("ALIVE_NAME", "🥀ƗŦ'Ş βΔĐ βØ¥ ✘ 🄿🄰🄿🄿🅄🍄")
BOT_USERNAME = getenv("BOT_USERNAME", "Team_Coder_Music_Bot")
OWNER_ID = getenv("OWNER_ID", "6230484593")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Samsari_boltey")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FRIENDZVIBES")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FRIENDZVIBES")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6063904500").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/dd3c08bd6b1820b14a6d0.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/6c32810401263be4efb61.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Sumit9969/NIXA-MUSIC-BOT")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/e53f65a49c4ee5553fab9.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/e53f65a49c4ee5553fab9.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
