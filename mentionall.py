import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []


from pyrogram import Client, filters, idle
fro

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**🤖Salam Mən [Usta Taggger Bot](http://t.me/ustataggerbot)-u.**\n**Qurupunuz'daki  bütün üzvləri tağ etmək səlahiyyətinə sahibəm.\n\n🤖Əmrlər üçün /help yazıb məndən kömək ala bilərsiniz.**",
                    buttons=(
               
		      [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/ustataggerbot?startgroup=a'), 
		       Button.url('➕ Usta Music Bot ➕','http://t.me/Ustamusicbot?startgroup=a')],
                      [Button.url('Qurup🛠', 'https://t.me/USTANAME'),
                       Button.url('Kanal📢', 'https://t.me/USTABOTLAR')],
		      [Button.url('Sahib👨‍💻', 'https://t.me/UstaNakhid'),],

                    
                     ),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "** [Usta Tagger Bot](http://t.me/UstaTaggerBot)-un Əmrlər.**\n\n**🤖 /tag <səbəb> - 5-li Tag Atışları.**\n**🤖 /etag <səbəb> - Emoji ilə etiketlər.**\n**🤖 /stag <səbəb> - Söz'lü Tag etiketlər.**\n**🤖 /tektag <səbəb> - Üzvləri Tək-Tək etiketlər.**\n**🤖 /usta <səbəb> - Usta Tagger Bot'una aid Tag etiketlər.**\n**🤖 /admins <səbəb> - İdarəçilər Tək-Tək etiketlər.**\n**🤖 /cancel - Tag Ələməyi Dayandır.**\n**🤖 /start - Botu işə salır**\n**🤖 /reklam - Reklam və ya əməkdaşlıq üçün bu əmrdən istifadə edin.**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/ustataggerbot?startgroup=a'), 

		       Button.url('➕ Usta Music Bot ➕','http://t.me/Ustamusicbot?startgroup=a')],

                      [Button.url('Qurup🛠', 'https://t.me/USTANAME'),

                       Button.url('Kanal📢', 'https://t.me/USTABOTLAR')],

		      [Button.url('Sahib👨‍💻', 'https://t.me/UstaNakhid'),],),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


# emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 

emoji = "😀 🐵 🍓 😃 🦁 🍒 😄 🐯 🍎 😁 🐱 🍉 😆 🐶 🍑 😅 🐺 🍊 😂 🐻 🥭 🤣 🐨 🍍 😭 🐼 🍌 😗 🐹 🌶 😙 🐭 🍇 😚 🐰 🥝 😘 🦊 🍐 🥰 🦝 🍏 🤩 🐮 🍈 🥳 🐷 🍋 🤗 🐽 🍄 🙃 🐗 🥕 🙂 🦓 🍠 ☺️ 🦄 🧅 😊 🐴 🌽 😏 🐸 🥦 😌 🐲 🥒 😉 🦎 🥬 🤭 🐉 🥑 😶 🦖 🥯 😐 🦕 🥖 😑 🐢 🥐 😔 🐊 🍞 😋 🐁 🌰 😛 🐀 🥔 😝 🐇 🧄 😜 🐈 🍆 🤪 🐩 🧇 🤔 🐕 🥞 🤨 🦮 🥚 🧐 🐕‍🦺 🧀 🙄 🐅 🥓 😒 🐆 🥩 😤 🐎 🍗 😠 🐖 🍖 🤬 🐄 🥙 ☹️ 🐂 🌯 🙁 🐃 🌮 😕 🐏 🍕 😟 🐑 🍟 🥺 🐐 🥨 😳 🦌 🥪 😬 🦙 🌭 🤐 🦥 🍔 🤫 🦘 🧆 😰 🐘 🥘 😨 🦏 🍝 😧 🦛 🥫 😦 🦒 🥣 😮 🐒 🥗 😯 🦍 🍲 😲 🦧 🍛 😱 🐪 🍜 🤯 🐫 🍢 😢 🐿️ 🥟 😥 🦨 🍱 😓 🦡 🍚 😞 🦔 🥡 😖 🦦 🍤 😣 🦇 🍣 😩 🐓 🦞 😫 🐔 🦪 🤤 🐣 🍘 🥱 🐤 🍡 😴 🐥 🥠 😪 🐦 🥮 🤢 🦉 🍧 🤮 🦅 🍨 🤧 🦜 🍫 🤒 🪱 🍪 😶‍🌫 🕊️ 🥜 🤠 🦢 🍭 🤑 🦩 🧈 🤤 🦃 🦚 🥵 🦆 🫑 🥶 🐧 🍥 🥸 🦈 🍦 🤓 🐳 🍳 😇 🐝 🥧 🤭 🐌 🥤 🤫 🦋 🍨".split(" ")
  


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Keçmiş mesajlar üçün tag edə bilmirəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Etiket Yapmak için sebeb yok! **")
  else:
    return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Tag əməliyyatı uğurla dayandırıldı!**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"✰ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"✰ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond(" **Tag əməliyyatı uğurla dayandırıldı! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**✰ - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"✰ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

stag = (
"https://te.legra.ph/file/50771de1bcd2e67af5ae4.jpg , https://te.legra.ph/file/50771de1bcd2e67af5ae4.jpg",
"Unutma; Hər gələn sevməz.. Və heç bir sevgili getməz",
"Heç bir ruhun ağrısı sənin dərdindən az deyil"
"Hər şeyi sınayıram, amma bacardığımı edirəm."
"Sevgi bir qadının həyatının bütün hekayəsidir, lakin bir kişinin macərasıdır."
"Xoşbəxtlik hər şeydən əvvəl bədən sağlamlığındadır."
"Nə qədər yaşadığımız deyil, necə yaşadığımız önəmlidir"
"Yer göy qurşağıdır, ağıl prizmadır, varlıq isə ağ şüadır."
"Hara gedəcəyinizi bilmirsinizsə, hansı yolla getməyinin əhəmiyyəti yoxdur."
"Həyatda ən qiymətli vaxtdır. Onu kimə hədiyyə etdiyinizə diqqət edin."
"Bir evin bütün pəncərələrini sındırıb, sonra qapını döyə bilməzsən."
"Xoşbəxtlik yaşadığın həyat tərzində deyil, həyata baxış tərzindədir."
"Unutma; hər insan sevməz.. Və heç bir sevgili ayrılmaz."
"Bu həyatda yarım nəfəs. Sevgidən başqa heç nə planlaşdırma...",
"Hər kəsə içindəki yaxşılıq qədər gözəl bir həyat arzulayıram."
"Gözəlliyi gözəl edən ədəbdir, ədəb isə gözəlliyi sevmək üçün səbəbdir!",
"Qızılgül qoxusu qızılgül verənin əlində qalır"
"Sənin axtardığın səni axtarandır."
"Hətta bir quş da payı qədər göydə qanad çırpar"
"Həyat ürək götürməyi bilməyənlərə əmanət deyil"
"Dürüst olmaqdan qorxma, ən çox itirəcəyiniz yanlış insanlar olacaq."
"İnsan qırılanda səs çıxaran ağac deyil."
"Öyrənmək həyatın yeganə sübutudur."
"Dünya əhalisi artdıqca insanların sayı da azalır".
"Layiq olmadığını düşündüyün insanlara əsla həqiqəti söyləmə."
"Allaha şükür ki, göy hələ heç bir pul kisəsinə sığmır."
"Özün ol. Artıq hamı alınıb."
"Ömrümü yandır, boğazımdakı düyünləri uddum."
"O, o qədər gözəl gülümsəyirdi ki, sevməsəm, israf olardı."
"Onun sevdiyi mən deyiləm. Bunun ağrısını sənə deyə bilmərəm."
"Onun sevdiyi mən deyiləm. Bunun ağrısını sənə deyə bilmərəm."
"Hər şeyə zamanla öyrəşirsən, amma heç vaxt bitmir."
"Əgər həqiqəti deyirsənsə, heç nə xatırlamağa ehtiyac yoxdur."
"Əvvəlcə həqiqəti de... Yoxsa kimsə sənin yerinə mütləq həqiqəti deyəcək."
"Kişilər daha güclü ola bilər, amma dözən qadınlardır."
"Ağrının resepti yoxdur",
"Bütün xəyallar gerçəkləşə bilər, əgər onların arxasınca getməyə cəsarətiniz varsa."
"Bu gizli sevgidir, dərdlərimi heç kimə deyə bilmərəm."
"Səncə sevgi hər şeyi bağışlayarmı, zamanla keçərmi?"
"Mənə siqaret lazımdır, sən də"
"Mən heç kimi tanımırdım, mən səndən daha özələm"
"Bir gün sevgi bitər, xatirələr qalır"
"Sevgi çox uzun bir sözdür!",
"Sən mənim xatırladığım ən unudulan şeysən."
"Birlikdə gülmək üçün darıxdığım insanlar var."
"Səndə xoşbəxtlik tapan sənindir, ondan kənarda qonaqdır."
"Çətin sev, amma sevmirsənsə məcbur etmə!",
"O, o qədər gözəl gülümsəyirdi ki, sevməsəm, israf olardı."
"və insan insana yoldaş olmalı, onun yaralarını sarmalıdır"
"Qəbiristanlıq ambisiyaya görə peşman olanlarla doludur"
"Sevgi külək kimidir, onu görə bilməzsən, amma hiss edə bilərsən."
"Tərəzi var, tərəzi var, hər şeyin vaxtı var"
"Ağıl kasıb olanda, ağıl təkəbbürlü olur."
"Günahsız baxışlara aldanma, hansısa şeytanın ayaq üstə alqışları...",
"Həyat sabahı gözləyəcək qədər uzun deyil"
"Yaxşılar heç vaxt itirmirlər, itirirlər."
"El vermədiyin sevgiyə möhtac olmağını arzu edirəm",
"Kaş ki, ağıl vermək əvəzinə mənə dinclik verəydin"
"Heç bilmədiyim qoxunun üçün darıxıram"
"İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟",
"𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑚𝑎 𝑠𝑚𝑎 𝑠𝑚𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑝
"𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖",
"Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑎𝑑ı 𝑎𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘",
"Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛 𝑢𝑦𝑎𝑛 𝑢𝑦𝑎𝑛 𝑢𝑦𝑎𝑛 𝑦𝒒𝑛 𝑖𝑛𝑛𝑛𝑛𝑛𝑝𝑝𝑝𝑝𝑝𝑝,
"𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ı𝑎𝑙𝑑ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑛ü𝑧ü 𝑎𝑙𝑧ü 𝑎𝑙𝑧ü 𝑎𝑙𝑧ü
"𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑛𝑛𝑛𝑛𝑛",
"İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟",
"𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑛𝑢 𝑣𝑒",
"𝑁𝑒𝑁𝑒𝑁𝑒𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒𝑑𝑑𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎",
"𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚 𝑑𝑎ℎ𝑖𝑙𝑖𝑚 𝑑𝑎ℎ𝑖𝑙𝑖𝑚",
"𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑚𝑎 𝑠𝑚𝑎 𝑠𝑚𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑝
"İşıq 𝑣𝑒 𝑎𝑛𝑙𝑎 işıq 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟",
"İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛",
"ÖS 𝑔Ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖𝑘𝑖𝑘𝑎𝑙𝑏𝑖𝑙𝑙𝑙𝑙𝑛 𝑘𝑎𝑑𝑎𝑟𝑘𝑎𝑑𝑎𝑟𝑔𝑧𝑒𝑙i𝑚",
"𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, içmək 𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛𝑏𝑎𝑧𝑒𝑛𝑏𝑎𝑧𝑒𝑛𝑦𝑦 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘Three𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟",
"𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖",
"Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑎𝑑ı 𝑎𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘",
"𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑖𝑟 𝑙𝑖𝑟 𝑙𝑖𝑟 𝑙𝑎❑ü𝑛𝑎𝑎𝑙",
"𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ağ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎",
"𝑉𝑒𝑟𝑖𝑙𝑒𝑛𝑉𝑒𝑟𝑖𝑙𝑒𝑛𝑉𝑒𝑟𝑖𝑙𝑒𝑛𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟",
"𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖ℎ𝑎𝑑𝑑𝑖𝑛𝑖𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑛ı",
"𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘 𝑦𝑎 𝑦𝑎 𝑦𝑎 𝑦𝑎 𝑔𝑒𝑟𝑖𝑦𝑒 𝑔𝑒𝑟𝑖𝑦𝑒 𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎",
"𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑛𝑛𝑛𝑛𝑛",
"𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝐾𝑎𝑟şı𝑚𝑎 çı𝑘𝑎𝑟𝑑",
"İşıq 𝑣𝑒 𝑎𝑛𝑙𝑎 işıq 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟",
"𝑌Ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚𝑡𝑎𝑚𝑜𝑟𝑡𝑎𝑠𝑛𝑑𝑎𝑛𝑑𝑎𝑦𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘𝑣𝑎𝑟𝑣𝑎𝑟𝑣𝑎𝑟𝑣𝑎𝑟,
"𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛𝑛𝑑𝑒𝑛𝑛𝑑𝑒𝑛 𝑦𝑒𝑛 𝑦𝑒𝑛 𝑦𝑒𝑛 𝑦𝑒𝑛 𝑦𝑒𝑎ş,
"𝐻𝑒𝑟 Ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ağ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚",
"𝐺Ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛",
"İŞ𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 Ş𝑒𝑦 𝑖𝑖ℎ𝑎𝑦ı 𝑏𝑖𝑟𝑏𝑖𝑟ℎ𝑎𝑦ı ℎ𝑎𝑏𝑒𝑟𝑏𝑖𝑟𝑎𝑙ı𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛𝑏𝑎𝑧𝑒𝑛𝑏𝑎𝑧𝑒𝑛𝑦𝑦 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘Three𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟",
"Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑛𝑘𝑢",
"𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑎𝑟, 𝐵𝑎𝑟, 𝐵𝑎𝑟,𝐵𝑎𝑟,
"𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑛𝑚𝑎 𝑖𝑛𝑎𝑛 𝑛𝑎𝑛 𝑛𝑎𝑛 𝑛𝑎𝑛 𝑛𝑎𝑛 𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛,
"𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖 𝑧𝑎𝑚𝑎𝑛 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑔𝑒𝑡𝑖𝑟𝑖𝑟",
"𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢."
)	


@client.on(events.NewMessage(pattern="^/stag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

 if tagadmin.pattern_match.group(1):
  seasons = tagadmin.pattern_match.group(1)
 else:
  seasons = ""

 chat = await tagadmin.get_input_chat()
 a_=0
 await tagadmin.delete()
 async for i in client.iter_participants(chat, filter=cp):
  if a_ == 500:
   break
  a_+=5
  await tagadmin.client.send_message(tagadmin.chat_id, "{} {}".format(i.first_name, i.id, seasons))
  sleep(0.5)


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)


# USTA TAGGER BONA AYID XUSUSI TAG

 @client.on(events.NewMessage(pattern="^/usta ?(.*)"))
 async def etag(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
cumle = ['Hardasan Nəfəs🥲','Gəlmirsən😒','Yenə Kimə Yazısan🤨','Çirkin Çocuq😌','Cikolatam😍','Aaa Səndə Burdasan😳','Al Sənə🤓👉🍫','Sevmirsən Məni?🙁','Haa Düz derisən?🧐','Bu Kimdir😁','Ol😒Gəlmə','Bax Sənə Nə Aldım😌👉🐒','Nə Gözəlsən🤢','Sən Kimsən🙄','Gəl 🤫','Ooo Çox Gözəlsin🤌🤐','Şəxsiyə Yaz😌','Gəl Görüm Hələ🧐','Ayib Olsun😫','Bezdim Səndən🥲','Bu Neçədir1⃣🙂','Nömrəni ver də Vpda yazışaq🙊','Bi Giləm😏','Dava edəx💪',]




 @client.on(events.NewMessage(pattern='/offline'))
 async def handler(event):
    # Kimsə "Salam" və başqa bir şey deyəndə cavab verin
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Sən mənə sahib deyilsən!__")
    await event.reply('**Bot İşləyir Narahat olmayın** \n @DegGixM')

     
          @client.on(events.NewMessage(pattern='/reklam'))
          async def handler(event):	
          await event.reply('🤖 [Usta Tagger Bot](http://t.me/Ustataggerbot)-unda Reklam Almaq Üzçün [ɴᴀᴋʜɪᴅ ᴜsᴛᴀ](https://t.me/UstaNakhid)-ilə Әlaqә Saxlayın.')
    


print(">> Bot işləyir narahat olmayın. @ThrHassan Məlumat almaq üçün <<")
client.run_until_disconnected()
