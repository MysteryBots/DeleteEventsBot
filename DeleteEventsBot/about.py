from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# About Message
@Client.on_message(filters.private & filters.command(["about"]))
async def about(delbot, msg):
    await msg.reply(
        text=Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_button),
    )
