def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@client.on(events.NewMessage(from_users=OWNER_ID, pattern="^/broadcast$"))
async def broadcast(client, message):
    to_send = get_arg(message)
    chats = load_chats_list()
    success = 0
    failed = 0
    for chat in chats:
        try:
            await brend.send_message(int(chat), to_send)
            success += 1
        except:
            failed += 1
            remove_chat_from_db(str(chat))
            pass
    await message.reply(f"Mesaj {success} gruba gönderildi. {failed} grub başarısız")
