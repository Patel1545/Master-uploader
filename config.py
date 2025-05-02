import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8123497179:AAH9YY_ATGxS6ZXgy6dlg0Rd_ghTMydO4Y8")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "29267685"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "9aea863501d41261e6c75ad565b6e1e1")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7916516048").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
