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


@MTG33.on_message(filters.command("start"))
async def start_cmd(Client, message):
    print("Hello i am a bot i am in developing by MTG33 boss for mor details type help")

@MTG33.on_message(filters.command("start"))
async def start_cmd(Client, message):
    print("developer contact : t.me/SAITAMA_SENSEI_BOSS ")




print("BOT IS READY")

MTG33.run()
