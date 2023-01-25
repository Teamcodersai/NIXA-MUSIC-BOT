import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "5941659598:AAFCJGzLnIYOBZz2fq2EiNgNolnFmuTphBk")
BOT_NAME = getenv("BOT_NAME", "『𖤍 Lêɠêɳ̃ᴅᴍᴜsɪᴄ࿐』➙ ꯭🇮🇳꯭"")
API_ID = int(getenv("API_ID", "6296490"))
API_HASH = getenv("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
OWNER_NAME = getenv("OWNER_NAME", "⏤͟͞ 𝙉𝙀𝙊 / αƒк [🇮🇳]𓆩🖤𓆪")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SexyyNeo")
ALIVE_NAME = getenv("ALIVE_NAME", "⏤͟͞ 𝙉𝙀𝙊 / αƒк [🇮🇳]𓆩🖤𓆪")
BOT_USERNAME = getenv("BOT_USERNAME", "IPMUSIXBOT")
OWNER_ID = getenv("OWNER_ID")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "┼⃖͢•🔥⃞⃪⃜🅐ĐĐł₵₮┼⃖͢฿ØɎ⎯꯭̽𓆩🖤𓆪")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FRIENDZVIBES")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FRIENDZVIBES")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5755312811").split()))
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
