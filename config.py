# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21187167")

API_HASH = os.environ.get("API_HASH", "f7c20f7bc2041887a70d62f94310e005")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6860649146:AAHwONXLYFxtC4BYfYqZiQ1m3mP7Thhifqc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "AkariWatanabeBots") 

            

DB_NAME = os.environ.get("DB_NAME", "AKARIRENAME")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://LUFFY2005:LUFFY2005@cluster0.3rtva3q.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/445001437a1b5be6ac892.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5512261555').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
