import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","8173444"))
    API_HASH = os.environ.get("API_HASH","8ce53801c1b49cd4d2fa108eb151b255")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5337183930:AAEQc8pbjleTSxzyjtS_GHYWfeVvcy4pEKo")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","sjashaic")
    BOT_NAME = os.environ.get("BOT_NAME","asjcioac")
    BOT_ID = int(os.environ.get("BOT_ID","1234567890-"))
    SUDO_USERS = os.environ.get("SUDO_USERS","234567890-").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","djscakc")
    OWNER_ID = int(os.environ.get("OWNER_ID","1234567890"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","sijcaoic")
