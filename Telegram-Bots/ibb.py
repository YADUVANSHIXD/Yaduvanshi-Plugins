#By @Silicon_Bot_Update 
#Distribute and edit it as your wish but please don't remove credit 😓😓
#By stealing Credit of Developer you will not become pro so try to give full credit to Developer 🥺🥺🥺

import requests
import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


# Replace with your actual imgbb API key
IMGBB_API_KEY = '####'

@Client.on_message(filters.command("imgbb") & filters.private)
async def imgbb_upload(bot: Client, update: Message):
    replied = update.reply_to_message
    if not replied:
        await update.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.")
        return

    if not (replied.photo or replied.video or replied.animation):
        await update.reply_text("Please reply to a photo, video, or GIF.")
        return

    text = await update.reply_text("<code>Downloading to My Server ...</code>", disable_web_page_preview=True)

#By @Silicon_Bot_Update 
#Distribute and edit it as your wish but please don't remove credit 😓😓
#By stealing Credit of Developer you will not become pro so try to give full credit to Developer 🥺🥺🥺

    media = await update.reply_to_message.download()

    await text.edit_text("<code>Downloading Completed. Now I am Uploading to imgbb ...</code>", disable_web_page_preview=True)

    # Uploading to imgbb
    try:
        with open(media, 'rb') as file:
            response = requests.post(
                f"https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}",
                files={"image": file}
            )
            response_data = response.json()

            if response_data['success']:
                image_url = response_data['data']['url']
            else:
                raise Exception(response_data['error']['message'])
    except Exception as error:
        print(error)
        await text.edit_text(f"Error: {error}", disable_web_page_preview=True)
        return

    # Clean up the downloaded file
    try:
        os.remove(media)
    except Exception as error:
        print(error)

    await text.edit_text(
        text=f"<b>Link:</b>\n\n<code>{image_url}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="Open Link", url=image_url),
                InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={image_url}")
            ],
            [
                InlineKeyboardButton(text="✗ Close ✗", callback_data="close")
            ]
        ])
    )

#By @Silicon_Bot_Update 
#Distribute and edit it as your wish but please don't remove credit 😓😓
#By stealing Credit of Developer you will not become pro so try to give full credit to Developer 🥺🥺🥺
