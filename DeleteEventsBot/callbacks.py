from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from Config import Config
from Data import Data


# Callbacks
@Client.on_callback_query()
async def _calls(delbot, callback_query):
	chat_id = callback_query.from_user.id
	message_id = callback_query.message.message_id
	# .lower() to test somethings..
	if callback_query.data.lower() == "home":
		user = await delbot.get_me()
		mention = user["mention"]
		await delbot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.START.format(callback_query.from_user.mention, mention),
			reply_markup=InlineKeyboardMarkup(Data.buttons),
		)
	if callback_query.data.lower() == "about":
		await delbot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.ABOUT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_button),
		)
	if callback_query.data.lower() == "help":
		await delbot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.HELP,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_button),
		)
	if callback_query.data.lower() == "deploy":
		await delbot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.DEPLOY,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_button),
		)
		""" More Plans """
