#(©)Codexbotz

import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from plugins.link_generator import get_short
from bot import Bot
from config import ADMINS, CHANNEL_ID, ECHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode
from datetime import datetime, timedelta


#def find_pic(fname):
   # if fname == "Punyavathi":
     #  pic = "https://graph.org/file/db5fd2caa68198b86a621.jpg"
   # else:
     #  pic = "https://graph.org/file/954f49350f9b6e52fa545.jpg" 
 #   return pic

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    
    e_pic = await client.send_photo(ECHANNEL_ID, photo="https://graph.org/file/954f49350f9b6e52fa545.jpg", caption=f"🔥please wait....")
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    Tlink = f"https://telegram.me/{client.username}?start={base64_string}"
    Slink = get_short(Tlink)
#   today= datetime.datetime.now()
    tomorrow = datetime.now() + timedelta(1)
#   ptoday= today.strftime("%d - %m - %Y")
    ptomorrow = tomorrow.strftime("%d - %m - %Y")
#   pweek = tomorrow.strftime("%A")
    media = message.video or message.document
    test_string = media.file_name
    spl_word = 'S'
    res = test_string.partition(spl_word)[0]
    fname = res[:-1]
   # pic = find_pic(fname)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("[A]Share URL", url=Tlink)]])
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("[B]Share URL", url=Tlink)]])
    
    await e_pic.edit(ECHANNEL_ID, photo="https://graph.org/file/db5fd2caa68198b86a621.jpg", caption="✅ Generated wait")
    await reply_text.edit(f"{fname}\n <b>▬▬▬▬▬▬▬ ❂ ▬▬▬▬▬▬▬▬</b>\n\n🗓𝐃𝐚𝐭𝐞:- <b>{ptomorrow}</b>\n\n      𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐛𝐲 :- @Dot_serials_bot \n\n                     ⚜️⚜️⚜️⚜️⚜️⚜️\nᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :-\n{Slink}\n{Slink}\n\n     👇👇 𝐇𝐨𝐰 𝐭𝐨 𝐨𝐩𝐞𝐧 𝐥𝐢𝐧𝐤👇👇\nhttps://t.me/+Sb5ro1gyhgY0NWM1\nhttps://t.me/+Sb5ro1gyhgY0NWM1", disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return
  
    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    Tlink = f"https://telegram.me/{client.username}?start={base64_string}"
    link = get_short(Tlink)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("[C]Share URL", url=Tlink)]])
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("[D]Share URL", url=Tlink)]])
    
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
