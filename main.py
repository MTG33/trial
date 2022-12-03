from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API_ID = int(environ.get('API_ID', "28061494"))
API_HASH = environ.get('API_HASH', "5f7c625731e89fa00a6b3906e1f894a7")
BOT_TOKEN = environ.get('BOT_TOKEN', "5834355850:AAEagWKMd80wfOk5Y__z7jq96eZ4y-VgbdM")

MTG33 = Client(
    name="MTG33",
    api_id=API_ID
    api_hash=API_HASH
    bot_token=BOT_TOKEN
)

START_BUTTONS = [[
    InlineKeyboardButton("📢JOIN CHANNEL FOR REPO📢 ", url="t.me/MTG33CHANNEL")
    ]]

@MTG33.on_message(filters.command("start"))
async def start_cmd(Client, message):
    await message.reply_photo(
        photo="https://telegra.ph/ttelegram-11-30"
        caption=f"""Hello {message.from_user.mention}.i am a bot by MTG33 type /help for more information"""
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
        )

HELP_BUTTONS = [[
    InlineKeyboardButton("📍 OWNER 📍 ", url="t.me/MTG33")
    ]]
@MTG33.on_message(filters.command("help"))
async def help_cmd(Client, message):
    await message.reply_text("developer contact : t.me/MTG33")
        reply_markup=InlineKeyboardMarkup(HELP_BUTTONS)



print("BOT IS READY")

MTG33.run()
