
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API credentials
API_ID = 24736076
API_HASH = "22fc694d8b2b4ded4350e3fe25807976"
BOT_TOKEN = "8047135374:AAHpMGYqt63yd1BThfzic4F0XmtY1XaHHRc"

# MongoDB URL
MONGO_DB_URI = "mongodb+srv://Music800:Music800@cluster0.3d2hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Telegram IDs
LOG_GROUP_ID = 7648822500
OWNER_ID = 7648822500

# Assistant string session (Pyrogram)
STRING1 = getenv("", "1BVtsOIMBu7HeqCdOl6j_045bCub9Iz8xigCi_p1ZHrtrgUGJr7UEWA2QoI4BCVdFTwgJRyaP5dIObD-mExVYraJU81nn2CHFnMEnrA5dcKcPR_zfH6zMV2b-NaegVzOEP93dT4RolHpOxNpPn24Ah4EEn9SZIZyXaleI55fPXXn7uiFckazg_f9oElVRpXPG7tRuhd74xbzcwnv5_S1p42AAi5FE0q2MLi_zmgXcZcPUxrztcqy0wxm3N10uDYDry3B1XNv8S05KqSutkNqnscnZPPIYTdeyFJdDklJ0MPd5_7_dP6qNSC9onHliFDgleu5Q8BdU-BD0dViSmZy1skcxPDey9uE=")
1"1BVtsOIMBu7HeqCdOl6j_045bCub9Iz8xigCi_p1ZHrtrgUGJr7UEWA2QoI4BCVdFTwgJRyaP5dIObD-mExVYraJU81nn2CHFnMEnrA5dcKcPR_zfH6zMV2b-NaegVzOEP93dT4RolHpOxNpPn24Ah4EEn9SZIZyXaleI55fPXXn7uiFckazg_f9oElVRpXPG7tRuhd74xbzcwnv5_S1p42AAi5FE0q2MLi_zmgXcZcPUxrztcqy0wxm3N10uDYDry3B1XNv8S05KqSutkNqnscnZPPIYTdeyFJdDklJ0MPd5_7_dP6qNSC9onHliFDgleu5Q8BdU-BD0dViSmZy1skcxPDey9uE="
# Heroku deployment (optional)
HEROKU_APP_NAME = getenv("music890")
HEROKU_API_KEY = "HRKU-AASPwj_e-UxMsoC_B0IjrBrTfyI-kwThSQK3cF5VQq3A_wifkcHiep43"

# Upstream Repo
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/rishabhops/alice")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # For private repo

# Support links
SUPPORT_CHANNEL = "https://t.me/English_speaking890"
SUPPORT_GROUP = "https://t.me/Hindi_890"

# Settings
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# Banned users
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg"
PING_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
PLAYLIST_IMG_URL = "https://graph.org/file/763a841a2ad5cbb1e2fc5.jpg"
STATS_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

# Duration Limit
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL Checks
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Must start with https://")

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit("[ERROR] - Your SUPPORT_GROUP url is wrong. Must start with https://")
