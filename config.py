import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA3zAJz8wcriAHneeAaEtph3Wtbd4qQeBkilzu3sdVGrs4bzyFKomHHS2fHL5pzQBCNov8EVwL34Hz47MViJvDmOK4iqyUntx5ggB-quVSJgN8kyiH4MnIJxgqcanga55zMU6Q8nPEMW6x5bE4x_llURYMgEffLcbvNm3OcdYCgmJ2nko8JEFYPmjCpLrYe_eiS3D_vBG-BF8_s1pxgALY54QxkR8SnET4wab7BSk0Vs1p5dlDneKul0MjpWMEbdObp-5sUwvTpNYjHGa3gP5Mu-A6KZhp1yMlPh65UiPs6yBjI48uZMkVCqvFXnLf3DaoEAtpe5dqhhxYWBHvRNvEpAAAAAWlv1vQA")
BOT_TOKEN = getenv("BOT_TOKEN", "6134730333:AAGDm9L9SFcs8fDJSvxo--HTOqHCteHySlg")
BOT_NAME = getenv("BOT_NAME", "🆃ҽαɱ 🅲σԃҽɾ 🅼υʂιƈ")
API_ID = int(getenv("API_ID", "22875242"))
API_HASH = getenv("API_HASH", "32eddce639c6fd7fe6a40db879dcb91c")
OWNER_NAME = getenv("OWNER_NAME", "Samsari boltey")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Believe_Bad_Boy")
ALIVE_NAME = getenv("ALIVE_NAME", "🥀ƗŦ'Ş βΔĐ βØ¥ ✘ 🄿🄰🄿🄿🅄🍄")
BOT_USERNAME = getenv("BOT_USERNAME", "Team_Coder_Music_Bot")
OWNER_ID = getenv("OWNER_ID", "6063904500")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Samsari_boltey")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TeamcodersTG")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TeamcodersTG")
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
