from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery



API_ID = "28061494"
API_HASH = "5f7c625731e89fa00a6b3906e1f894a7"
BOT_TOKEN = "5834355850:AAEagWKMd80wfOk5Y__z7jq96eZ4y-VgbdM"

MTG33 = Client(
    name="MTG33",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_BUTTONS = [[
   InlineKeyboardButton("📢 JOIN CHANNEL FOR REPO", url="t.me/MTG33BOTZ"
]]

@MTG33.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hey !! {message.from_user.mention} ... I am a pyrogram Bot Created By @MTG33"),
    reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )

ABOUT_BUTTONS = [[
   InlneKeyboardButton("🔥 OWNER 🔥", url="t.me/MTG33"
]]

@MTG33.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/a205efc04302b22bc358b.jpg",
        caption="MY REPO: github/MTG33/trial \n MY DEPLOYER : @MTG33 👇",
        reply_markup=InlineKeyboardMarkup(ABOUT_BUTTONS)
    )




print(" © BOT DEPLOYED © ")

MTG33.run()
