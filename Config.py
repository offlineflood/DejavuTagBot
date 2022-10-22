import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","16157584"))
    API_HASH = os.environ.get("API_HASH","2167d4e6007a79eed91d084bf5b8966a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5337183930:AAEQc8pbjleTSxzyjtS_GHYWfeVvcy4pEKo")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","dejavy")
    BOT_NAME = os.environ.get("BOT_NAME","jhkoijl")
    BOT_ID = int(os.environ.get("BOT_ID","234567890-"))
    SUDO_USERS = os.environ.get("SUDO_USERS","rseyutiydou").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","ioj")
    OWNER_ID = int(os.environ.get("OWNER_ID","43567890"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","uijio;kl,")
