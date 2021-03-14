from pyrogram import Client, filters


# Delete Service Messages
@Client.on_message(filters.group & filters.service)
async def delservice(delbot, msg):
    chat_member = await delbot.get_chat_member(msg.chat.id, "self")
    if chat_member.status == "administrator":
        if chat_member.can_delete_messages:
            await msg.delete()
        else:
            await msg.reply(
                "I'm surely admin, but I don't have 'delete messages' permission !!"
            )
    else:
        await msg.reply(
            "I'm not admin, so I can't delete messages. Add me again and make me admin this time if you need my help. Leaving...."
        )
        await msg.chat.leave()
