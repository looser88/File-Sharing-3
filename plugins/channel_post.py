#(©)Codexbotz

#import re
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.errors import FloodWait
from plugins.link_generator import get_short
from bot import Bot
from config import ADMINS, CHANNEL_ID, ZEE_ID, VOOT_ID, STAR_ID, ECHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode
from datetime import datetime, timedelta

#@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.text & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
#def find_pic(message: Message):

  #  spl_word = 'S' 
 #   media = message.video or message.document
#    full_str = message.video.file_name
 #   res = re.split('S', msg.video.file_name, maxsplit=1)[0]
  #  return res

#def find_pic(extract_name): 
#    if extract_name == "Olavina_Nildana_2023_":
#       pic = "https://graph.org/file/db5fd2caa68198b86a621.jpg"
#    else:
#       pic = "https://graph.org/file/9ec8c13d8c10d246a60ba.jpg" 
#    return pic

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    media = message.video or message.document
    if "Zee5"or"ZEE5" in media.file_name:
       chatidis = int("-1001942664190")
    elif "Voot"or"VOOT" in media.file_name:
         chatidis = VOOT_ID
    elif "HS"or"Hotstar" in media.file_name:
         chatidis = STAR_ID
    else:
        chatidis = ECHANNEL_ID
        
     #if candition for photo 
    if "Olavina_Nildana" in media.file_name:
       pic = "https://graph.org/file/db5fd2caa68198b86a621.jpg"
    else:
       pic = "https://graph.org/file/9ec8c13d8c10d246a60ba.jpg" 
  

    reply_text = await message.reply_text("Please Wait...!", quote = True)
    e_pic = await client.send_photo(f"{chatidis}", photo=f"{pic}", caption=f"🔥please wait....")
    await asyncio.sleep(3)
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
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("[A]Share URL", url=Tlink)]])
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("[B]Share URL", url=Tlink)]])
    
    
    await reply_text.edit(f"✅link generated successfully. \n\n name :{media.file_name}\n\n check your \nECHANNEL: https://t.me/+BoY5HamXAd1kOTZl\n\n here your link:\n{Tlink}", disable_web_page_preview = True)
    await e_pic.edit(f" <b>▬▬▬▬▬▬▬ ❂ ▬▬▬▬▬▬▬▬</b>\n\n🗓𝐃𝐚𝐭𝐞 :- <b>{ptomorrow}</b>\n\n      𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐛𝐲 :- @Dot_serials_bot \n\n                     ⚜️⚜️⚜️⚜️⚜️⚜️\nᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :-\n{Slink}\n{Slink}\n\n     👇👇 𝐇𝐨𝐰 𝐭𝐨 𝐨𝐩𝐞𝐧 𝐥𝐢𝐧𝐤👇👇\nhttps://t.me/+Sb5ro1gyhgY0NWM1\nhttps://t.me/+Sb5ro1gyhgY0NWM1")
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
