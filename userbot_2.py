from telethon import TelegramClient, events

api_id = '26993697'
api_hash = '4e01bdf8049b3c716ba2ce96b9238886'

ADMIN_IDS = [1507577220]  # Ganti dengan user_id admin kamu
MESSAGE_TEXT = "Yang gabut sini gabung ke bio ngobrol santai becek😜😜"
bot_active = False
sent_groups = set()

client = TelegramClient('userbot_session', api_id, api_hash)

EXCLUDED_GROUPS = [-1002260433857, -1001705932491]  # Ganti dengan chat_id grup yang ingin DIKECUALIKAN

@client.on(events.NewMessage)
async def handler(event):
    global bot_active, sent_groups

    # Hanya proses pesan text
    if not event.raw_text:
        return

    # Panel admin: hanya admin yang bisa on/off bot
    if event.sender_id in ADMIN_IDS and event.raw_text.startswith('.bot'):
        cmd = event.raw_text.split()
        if len(cmd) > 1:
            if cmd[1] == 'on':
                bot_active = True
                sent_groups.clear()
                await event.respond("Userbot diaktifkan.")
            elif cmd[1] == 'off':
                bot_active = False
                await event.respond("Userbot dimatikan.")
            elif cmd[1] == 'status':
                await event.respond(f"Userbot aktif: {bot_active}")
            else:
                await event.respond("Perintah: .bot on | .bot off | .bot status")
        return

    # Jika bot aktif, pesan dari siapapun, hanya kirim 1x per grup, dan TIDAK di grup yang dikecualikan
    if (
        bot_active
        and event.is_group
        and event.chat_id not in sent_groups
        and event.chat_id not in EXCLUDED_GROUPS
    ):
        await client.send_message(event.chat_id, MESSAGE_TEXT)
        sent_groups.add(event.chat_id)
        # Kirim info ke admin
        for admin_id in ADMIN_IDS:
            try:
                await client.send_message(
                    admin_id,
                    f"✅ Pesan berhasil dikirim ke grup:\nNama: {event.chat.title}\nchat_id: {event.chat_id}"
                )
            except Exception as e:
                print(f"Gagal kirim info ke admin: {e}")
# (Block removed because it was a duplicate and caused an indentation error)

client.start()
print("Userbot aktif. Tekan Ctrl+C untuk keluar.")
client.run_until_disconnected()