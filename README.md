# Telegram Userbot (Telethon)

Userbot ini akan mengirim pesan otomatis ke grup Telegram (kecuali grup yang dikecualikan) dan dapat dikontrol on/off oleh admin melalui perintah chat.

---

## Fitur
- Kirim pesan otomatis ke semua grup (kecuali yang dikecualikan)
- Hanya kirim 1x per grup per sesi aktif
- Panel admin: aktifkan/matikan bot lewat perintah `.bot on` / `.bot off`
- Notifikasi ke admin jika pesan berhasil/gagal dikirim ke grup

---

## Cara Menjalankan

1. **Clone repo & install dependensi**
    ```bash
    git clone <repo-anda>
    cd <repo-anda>
    pip install telethon
    ```

2. **Edit file `userbot_2.py`**
    - Isi `api_id` dan `api_hash` (lihat cara dapatkan di bawah)
    - Isi `ADMIN_IDS` dengan user_id admin kamu
    - Isi `EXCLUDED_GROUPS` dengan chat_id grup yang ingin dikecualikan

3. **Jalankan userbot**
    ```bash
    python userbot_2.py
    ```
    Saat pertama kali dijalankan, login dengan nomor Telegram kamu dan masukkan kode OTP.

---

## Cara Mendapatkan API ID & API Hash

1. Buka [https://my.telegram.org](https://my.telegram.org) di browser.
2. Login dengan nomor Telegram kamu.
3. Pilih **API development tools**.
4. Buat aplikasi baru, lalu catat **API ID** (angka) dan **API Hash** (string panjang).
5. Masukkan ke dalam script:
    ```python
    api_id = 1234567
    api_hash = 'abcdef1234567890abcdef1234567890'
    ```

---

## Cara Mendapatkan User ID Admin

1. Buka Telegram, cari dan chat dengan [@userinfobot](https://t.me/userinfobot).
2. Kirim pesan `/start`.
3. Bot akan membalas dengan user ID kamu.
4. Masukkan ke dalam `ADMIN_IDS` di script:
    ```python
    ADMIN_IDS = [123456789]
    ```

---

## Cara Mendapatkan Chat ID Grup (dan Mengecualikan Grup)

**Opsi 1: Pakai @getidsbot**
1. Invite [@getidsbot](https://t.me/getidsbot) ke grup kamu.
2. Ketik `/getid` di grup.
3. Catat chat_id grup (format: `-100xxxxxxxxxx`).

**Opsi 2: Pakai Script Telethon**
```python
from telethon import TelegramClient

api_id = 'API_ID_KAMU'
api_hash = 'API_HASH_KAMU'
client = TelegramClient('session', api_id, api_hash)

async def main():
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            print(f"{dialog.name}: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
```
Jalankan script di atas, semua chat_id grup kamu akan tampil di terminal.

**Masukkan ke dalam `EXCLUDED_GROUPS`:**
```python
EXCLUDED_GROUPS = [-1001234567890, -1009876543210]
```

---

## Catatan
- Jalankan userbot dengan akun Telegram biasa (bukan bot token).
- Jangan gunakan untuk spam agar akun tidak diblokir Telegram.
- Untuk keamanan, **jangan upload api_id/api_hash ke publik**.

---

## Lisensi
Bebas digunakan dan dikembangkan kembali.
