from pyrogram import idle
from pyrogram import Client as Bot
from modules.clientbot import run
from modules.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    string_session=STRING_SESSION,
    plugins=dict(root="plugins")
)

bot.start()
run()
idle()
