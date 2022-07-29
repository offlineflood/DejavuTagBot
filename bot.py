#
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

    @app.on_message(filters.command(["start", "help"]))
    async def start_command(_, message: Message):
        if await mongo.is_banned_user(message.from_user.id):
            return
        await mongo.add_served_user(message.from_user.id)
        await message.reply_text(config.PRIVATE_START_MESSAGE)

    @app.on_message(
        filters.command("mode") & filters.user(SUDO_USERS)
    )
    async def mode_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var müəyyən edilməyib. Zəhmət olmasa əvvəlcə onu müəyyənləşdirin."
            )
        usage = "**İstifadə:**\n\n/rejim [qrup | şəxsi]\n\n**Qrup**: Bütün gələn mesajlar Giriş qrupuna yönləndiriləcək.\n\n**Şəxsi**: Bütün gələn mesajlar SUDO_USERS Şəxsi Mesajlarına yönləndiriləcək"
        if len(message.command) != 2:
            return await message.reply_text(usage)
        state = message.text.split(None, 1)[1].strip()
        state = state.lower()
        if state == "group":
            await mongo.group_on()
            await message.reply_text(
                "Qrup Rejimi Aktivdir. Bütün daxil olan mesajlar LOG Group-a yönləndiriləcək"
            )
        elif state == "private":
            await mongo.group_off()
            await message.reply_text(
                "Şəxsi Rejim Aktivdir. Bütün gələn mesajlar bütün SUDO_USER-lərin Şəxsi Mesajına yönləndiriləcək"
            )
        else:
            await message.reply_text(usage)

    @app.on_message(
        filters.command("block") & filters.user(SUDO_USERS)
    )
    async def block_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var müəyyən edilməyib. Zəhmət olmasa əvvəlcə onu müəyyənləşdirin"
            )
        if message.reply_to_message:
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
            if await mongo.is_banned_user(replied_user_id):
                return await message.reply_text("Artıq Blok edilib")
            else:
                await mongo.add_banned_user(replied_user_id)
                await message.reply_text("Botdan Qadağan edilmiş İstifadəçi")
                try:
                    await app.send_message(
                        replied_user_id,
                        "İndi adminlər tərəfindən Botdan istifadə etmək sizə qadağa qoyulub.",
                    )
                except:
                    pass
        else:
            return await message.reply_text(
                "İstifadəçinin botdan istifadəsinə mane olmaq üçün onun yönləndirilmiş mesajına cavab verin"
            )

    @app.on_message(
        filters.command("unblock") & filters.user(SUDO_USERS)
    )
    async def unblock_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var müəyyən edilməyib. Zəhmət olmasa əvvəlcə onu müəyyənləşdirin"
            )
        if message.reply_to_message:
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
            if not await mongo.is_banned_user(replied_user_id):
                return await message.reply_text("Artıq Blokdan Çıxarılıb")
            else:
                await mongo.remove_banned_user(replied_user_id)
                await message.reply_text(
                    "Botdan blokdan çıxarılan istifadəçi"
                )
                try:
                    await app.send_message(
                        replied_user_id,
                        "İndi adminlər tərəfindən Botdan bloklanmısınız.",
                    )
                except:
                    pass
        else:
            return await message.reply_text(
                "İstifadəçini botdan blokdan çıxarmaq üçün onun yönləndirilmiş mesajına cavab verin"
            )

    @app.on_message(
        filters.command("stats") & filters.user(SUDO_USERS)
    )
    async def stats_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var müəyyən edilməyib. Zəhmət olmasa əvvəlcə onu müəyyənləşdirin"
            )
        served_users = len(await mongo.get_served_users())
        blocked = await mongo.get_banned_count()
        text = f""" **DegGxiM Statistikası :**
        
**Python versiyası :** {pyver.split()[0]}
**Piroqram versiyası :** {pyrover}

**Xidmət edilən İstifadəçilər :** {served_users} 
**Bloklanmış İstifadəçilər :** {blocked}"""
        await message.reply_text(text)

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
                    message.text == "/unblock"
                    or message.text == "/block"
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
                message.text == "/unblock"
                or message.text == "/block"
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
