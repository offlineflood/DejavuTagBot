from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime


app = Client(
    "MentionAll",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

#@app.on_message(filters.command("start"))
#async def _py(client: Client, message: Message):
 #   await message.reply_text('Pyrogram is a Python library for Telegram bots.')

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`**🤖Salam` {msg.from_user.mention} `\n🤖Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər⚡️`\n\n🤖Qurup'da User'ləri Tag Edmə Xususiyətinə Malik'əm.
Ətraflı Məlumat üçün /help-ə toxunun.**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('[UstaTaggerBot](https://t.me/Ustataggerbot)-un Sahibi Qurupa Qatildı.\n\nXoş Gəldin Sahib😍.')

 
@app.on_message(filters.command("id"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**İstifadəçi Məlumatı:**\n"
    out_str += f" ⚡️ __Qrup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 💎 __İstifadəçi Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj ID-si__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Cavab verilmiş İstifadəçi ID__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)

#@app.on_message(filters.command("info"))
#async def _id(_, message: Message):
  #  msg = message.reply_to_message or message
 #   out_str = "**User İnfo:**\n"
  #  out_str += f" ⚡️ __Grup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
   # out_str += f" 💎 __Yanıtlanan Kullanıcı Adı__ : {msg.from_user.first_name}\n"
    #out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    #if msg.from_user:
     #   out_str += f" 🙋🏻‍♂️ __Yanıtlanan Kullanıcı ID__ : `{msg.from_user.id}`\n"
 
    #await message.reply(out_str)

#@app.on_message(filters.command("ping"))
#async def pingy(client, message):
  #  start = datetime.now()
 #   hmm = await message.reply("Pong!")
#    end = datetime.now()
   # ms = (end - start).microseconds / 1000
  #  await hmm.edit(
 #       f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\n**Ping: {round(ms)}**")
    
app.start()
print(f"Bot pyrogram ( {pyrogram.__version__} sürümü ile başlatıldı. ")
idle()
