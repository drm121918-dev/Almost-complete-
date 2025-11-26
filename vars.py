from os import environ

PORT = int(environ.get("PORT", 8870))

API_ID = int(environ.get("API_ID", "36925285"))
API_HASH = environ.get("API_HASH", "ef3e2c581370c93287854dc36d78c13c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

DATABASE_URL = environ.get("mongodb+srv://drm121918_db_user:<db_KtwMBKSvKo56817L>@almostcomplete.vxtrirx.mongodb.net/?appName=Almostcomplete", "mongodb://localhost:27017/your_bot_db")

