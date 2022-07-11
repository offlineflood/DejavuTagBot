import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_NAME = os.environ.get("BOT_NAME")
    BOT_ID = int(os.environ.get("BOT_ID"))
    SUDO_USERS = os.environ.get("SUDO_USERS").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT")
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
