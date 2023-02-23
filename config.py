import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6435225")
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    TOKEN = getenv("TOKEN", "6206483292:AAEC5ql3ww3Ve18UaTrDVC7a_HyqWlJCIf8")
    OWNER_ID = getenv("OWNER_ID", "1963316264")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "2119484425")
    STRING_SESSION = getenv("STRING_SESSION", "1AZWarzgBu46cjFTJZ0GyvXa-naTz7G5GQlyVIc8094uq_-w8iB9HDIH9Vq8jzxvaCGYFwLrdISvep8R8VqwQtMFSNixtyOfSKQzBqJkOnymL28ux_DXHM0QzNUzbSPEpHRiQS9J6JTQdiUpHHc_fkuchkBoLUxDqXheGzw5XDiI7mkWI_uNSOEuy5qWHhXFFOeX5yA_r1zSr3q4uDqOdYK6BUE1lF9k-6KCgteDMqjSFzt3-nqN1tk4nOM2P60AgFATYcBHgQWm9ME9P1H_CbgeBC1QmMrk5gyFFRrFY3oJFdD7XNqW6L0TnLU5jqUYlOLfOB6Ytp927dxmoACTlRtEOmHfmNpc=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "")
    DB_URI = getenv("DATABASE_URL", "postgres://bbaqvyvy:OoVdbd1ACTcYRmZKktfqLxmzY_jhmWL5@suleiman.db.elephantsql.com/bbaqvyvy")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001895648978")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001895648978")
    SYS_ADMIN = getenv("SYS_ADMIN", "1963316264")
    DEV_USERS = getenv("DEV_USERS", "19633162764")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "TheUpdatesChannel")
    SUPPORT = getenv("SUPPORT", "TheSupportChat")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
