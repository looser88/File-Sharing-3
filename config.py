#(©)CodeXBotz



from os import environ
import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6180766269:AAF0jG2fxEc6iu19Ps8HFAQYa3lmQbtyTeg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10755921"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d5e49fd3637cba407f17807d31c77977")

#channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001842556179")) #db channel 
ZEE_ID = int(os.environ.get("ZEE_ID", "-1001454521684"))
VOOT_ID = int(os.environ.get("VOOT_ID", "-1001328262780"))
STAR_ID = int(os.environ.get("STAR_ID", "-1001658231983"))
ECHANNEL_ID = int(os.environ.get("EHANNEL_ID", "-1001748750847"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5636224141"))

#Port
PORT = os.environ.get("PORT", "8080")

#shortner
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'Fire-links.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '4b4ee8f8717d775262ef74432e202b8be8597b62')

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://cheesy:cheesy.8697@cluster0.kjg8cfb.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "fileshare2")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1147676731").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>📁ғɪʟᴇ ɴᴀᴍᴇ</b> : <code>{filename}</code> \n<b>\n🎬Jᴏɪɴ ᴜs :<a href='https://t.me/dot_serials'>𝐃𝐎𝐓 𝐒𝐄𝐑𝐈𝐀𝐋𝐒</a>\n</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5636224141)
ADMINS.append(1284476297)
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
