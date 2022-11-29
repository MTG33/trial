from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""


MTG33 = Client(
    name="MTG33",
    api_id=API_ID
    api_hash=API_HASH
    bot_token=BOT_TOKEN
)


print("BOT IS READY")

MTG33.run()
