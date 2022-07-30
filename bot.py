# dikkat bu hesse tam hazir deyli deye herakuda buna gora xera verecex burani sil!,  ve start fayilna ged bunun adin da ordan sil! ondan sonra depolar. ugur olsun!

# Müəllif hüququ (C) 2021-2022 by offlineflood@Github, < https://github.com/ChatBot >.
#
# Bu faylın bir hissəsidir < https://github.com/offlineflood/ChatBot > layihə,
# və "GNU v3.0 Lisenziya Müqaviləsi" əsasında buraxılır".
# Zəhmət olmasa baxın < https://github.com/offlineflood/ChatBot/blob/master/LICENSE >
#
# Bütün hüquqlar qorunur.
#

import asyncio
from sys import version as pyver

import pyrogram
from pyrogram import __version__ as pyrover
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import Message

import config
import mongo
from mongo import db

loop = asyncio.get_event_loop()
SUDO_USERS = config.SUDO_USER

app = pyrogram.Client(
    ":DegGxiM:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

save = {}
grouplist = 1


async def init():
    await app.start()


    
    
    
    
    
    
        @app.on_message(
        filters.command("broadcast") & filters.user(SUDO_USERS)
    )
    async def broadcast_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var müəyyən edilməyib. Zəhmət olmasa əvvəlcə onu müəyyənləşdirin"
            )
        if message.reply_to_message:
            x = message.reply_to_message.message_id
            y = message.chat.id
        else:
            if len(message.command) < 2:
                return await message.reply_text(
                    "**İstifadə**:\n/broadcast [MESSAGE] və ya [Mesajı Cavab]"
                )
            query = message.text.split(None, 1)[1]

        susr = 0
        served_users = []
        susers = await mongo.get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                await app.forward_messages(
                    i, y, x
                ) if message.reply_to_message else await app.send_message(
                    i, text=query
                )
                susr += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                pass
        try:
            await message.reply_text(
                f"**Mesajı yayımlayın {susr} İstifadəçilər.**"
            )
        except:
            pass

    @app.on_message(filters.private & ~filters.edited)
    async def incoming_private(_, message):
        user_id = message.from_user.id
        if await mongo.is_banned_user(user_id):
            return
        if user_id in SUDO_USERS:
            if message.reply_to_message:
                if (
                    #message.text == "/unblock"
                   # or message.text == "/block"
                    or message.text == "/broadcast"
                ):
                    return
                if not message.reply_to_message.forward_sender_name:
                    return await message.reply_text(
                        "Yalnız yönləndirilmiş mesajlara cavab verin."
                    )
                replied_id = message.reply_to_message_id
                try:
                    replied_user_id = save[replied_id]
                except Exception as e:
                    print(e)
                    return await message.reply_text(
                        "İstifadəçini əldə etmək alınmadı. Siz botu yenidən işə salmısınız və ya xəta baş verib. Zəhmət olmasa qeydləri yoxlayın"
                    )
                try:
                    return await app.copy_message(
                        replied_user_id,
                        message.chat.id,
                        message.message_id,
                    )
                except Exception as e:
                    print(e)
                    return await message.reply_text(
                        "Mesajı göndərmək alınmadı, İstifadəçi botu bloklamış və ya səhv bir şey baş vermiş ola bilər. Zəhmət olmasa qeydləri yoxlayın"
                    )
        else:
            if await mongo.is_group():
                try:
                    forwarded = await app.forward_messages(
                        config.LOG_GROUP_ID,
                        message.chat.id,
                        message.message_id,
                    )
                    save[forwarded.message_id] = user_id
                except:
                    pass
            else:
                for user in SUDO_USERS:
                    try:
                        forwarded = await app.forward_messages(
                            user, message.chat.id, message.message_id
                        )
                        save[forwarded.message_id] = user_id
                    except:
                        pass

    @app.on_message(
        filters.group & ~filters.edited & filters.user(SUDO_USERS),
        group=grouplist,
    )
    async def incoming_groups(_, message):
        if message.reply_to_message:
            if (
                #message.text == "/unblock"
               # or message.text == "/block"
                or message.text == "/broadcast"
            ):
                return
            replied_id = message.reply_to_message_id
            if not message.reply_to_message.forward_sender_name:
                return await message.reply_text(
                    "Yalnız yönləndirilmiş mesajlara cavab verin."
                )
            try:
                replied_user_id = save[replied_id]
            except Exception as e:
                print(e)
                return await message.reply_text(
                    "İstifadəçini əldə etmək alınmadı. Siz botu yenidən işə salmısınız və ya xəta baş verib. Zəhmət olmasa qeydləri yoxlayın"
                )
            try:
                return await app.copy_message(
                    replied_user_id,
                    message.chat.id,
                    message.message_id,
                )
            except Exception as e:
                print(e)
                return await message.reply_text(
                    "Mesajı göndərmək alınmadı, İstifadəçi botu bloklamış və ya səhv bir şey baş vermiş ola bilər. Zəhmət olmasa qeydləri yoxlayın"
                )

    print("[LOG] - DegGixM Akdifdir Başladı")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
