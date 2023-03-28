import os , requests , re , asyncio , redis
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import Client
from pyrogram.filters import command
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)
r = redis.from_url('redis://')
R = redis.Redis(charset="utf-8", decode_responses=True)
##########//((Dev JABWA))//##########
api_id = 15296051
bot_id = 6286232220
api_hash = "4c3e35efa89e4a71172e986f80f57c7b"
token = "6286232220:AAHtLGg4vWLlyZXVFqt2kULmkLigV4LgRbY"
app = Client("JABWA", bot_token=token,api_id=api_id,api_hash=api_hash)
##########//((Dev JABWA))//##########
@app.on_message(filters.regex("قفل كيبورد الصانع") & filters.user(1965534755))
async def Saidi(_, message: Message):
    await message.reply_text("**⋆ تم حذف كيب الصانع بنجاح\n√**",quote=True,reply_markup=ReplyKeyboardRemove(selective=True))
@app.on_message(filters.regex("/start") & filters.user(1965534755))
async def Saidi(_, message: Message):
    JABWA = ReplyKeyboardMarkup([
["قفل كيبورد الصانع"],
["صنع بوت","حذف بوت"],
["تحديث الصانع"]],resize_keyboard=True)
    await message.reply_text("**⋆ اهلا بك , عزيزي المطور الاساسي 🧑‍✈️**",reply_markup=JABWA,quote=True)
#######//((Dev JABWA))//#######
@app.on_message(filters.regex("صنع بوت") & filters.user(1965534755))
async def Saidi(_, message: Message):
    saidi ="""
from pyrogram import enums
API_ID = 793178
API_HASH = "9f4461079f30757ca0a4c23e14bd523f"
TOKEN = "5939167728:AAGjLsLXHPhFw8pgmqwNut5noFOReCck9e0"
BOT_ID = 5939167728
BOT_USERNAME = "Vpsi1bot"
CHANNEL = "updateLaith"
SUDO = "1965534755"
"""
    f = open("./maker/config.py","w")
    f.write(saidi)
    f.close()
    os.system(f"cp -a ./maker/. ./{message.from_user.id} && cd {message.from_user.id} && chmod +x * && screen -d -m -S {message.from_user.id} ./Run")
    await message.reply_text(f"**⋆ تم تنصيب البوت بنجاح\n√**",message.id)

@app.on_message(filters.regex("حذف بوت") & filters.user(1965534755))
async def Saidi(_, message: Message):
    os.system(f"sudo rm -fr {message.from_user.id}")
    os.system(f"screen -X -S {message.from_user.id} quit")
    await message.reply_text(f"**⋆ تم حذف البوت بنجاح\n√**",message.id)

@app.on_message(filters.regex("تحديث الصانع") & filters.user(1965534755))
async def Saidi(_, message: Message):
    Files = ["Saidi.py"]
      for update in Files:
      url = "https://raw.githubusercontent.com/VeerCli/VeerV2/master/"+update
      out = requests.get(url).text
      f = open("./"+update,"w+")
      f.write(out)
      f.close()
      await message.reply_text(f"**⋆ تم تحديث الصانع بنجاح\n√**",message.id)

@app.on_message(filters.regex("تيست") & filters.user(1965534755))
async def Saidi(_, message: Message):
    r.set("{}:{}:Type".format(bot_id,message.from_user.id),"settxt")
    await message.reply_text("ارسل", quote=True)

    if message.text and r.get("{}:{}:Type".format(bot_id,message.from_user.id)) == "settxt":
      r.set("{}:{}:title".format(bot_id,message.from_user.id),message.text)
      r.delete("{}:{}:Type".format(bot_id,message.from_user.id))
      await message.reply_text("تم حفظ الكليشه بنجاح", quote=True)


@app.on_message(filters.regex("بلح") & filters.user(1965534755))
async def Saidi(_, message: Message):
    jabwa = r.get("{}:{}:title".format(bot_id,message.from_user.id))
    await message.reply_text(f"**{jabwa}**",message.id)
##########//((Dev JABWA))//##########
print(""" 
▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌    ▐░▌     
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌    ▐░▌     
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌    ▐░▌     
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌    ▐░▌     
          ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌    ▐░▌     
 ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░

╔━━━━━━━━━━━━━━━━━━╗
┃Developer Source -» @JABWA
╠━━━━━━━━━━━━━━━━━━╣
┃Channel Source -» @S_a_i_d_i
╚━━━━━━━━━━━━━━━━━━╝
""")
app.run()