from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API_ID = "28061494"
API_HASH = "5f7c625731e89fa00a6b3906e1f894a7"
BOT_TOKEN = "5834355850:AAEagWKMd80wfOk5Y__z7jq96eZ4y-VgbdM"


MTG33 = Client(
    name="MTG33",
    api_id=API_ID
    api_hash=API_HASH
    bot_token=BOT_TOKEN
)


@MTG33.on_message(filters.command("start"))
async def start_cmd(Client, message):
    await message.reply_photo(
        photo="https://telegra.ph/ttelegram-11-30"
        caption="Hello i am a bot by MTG33 type /help for more information"

@MTG33.on_message(filters.command("help"))
async def help_cmd(Client, message):
    await message.reply_text("developer contact : t.me/MTG33")




print("BOT IS READY")

MTG33.run()
