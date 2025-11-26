# Don't Remove Credit Tg - @Tushar0125
# Ask Doubt on telegram @Tushar0125

from os import environ
👉 vars.py ফাইলের একদম উপরে এই লাইনটা যোগ করুন:


API_ID = int(environ.get("API_ID", "36925285")) #Replace with your api id
API_HASH = environ.get("API_HASH", "ef3e2c581370c93287854dc36d78c13c") #Replace with your api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "") #Replace with your bot token

PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set

