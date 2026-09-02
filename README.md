# Telegram Auto Message Purger

A lightweight Python script that automatically and securely purges your own messages from Telegram groups using the official Telegram MTProto API.

## Features

* Filters and deletes only messages sent by your account.
* Includes a built-in delay mechanism and properly handles `FloodWaitError` to prevent hitting Telegram rate limits.
* Keeps sensitive API credentials and target group configurations secure using environment variables (`.env`).

## Setup & Installation

1. **Clone the repository:**
```bash
git clone <REPO_URL>
cd <FOLDER_NAME>
```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
Rename `.env.example` to `.env` and fill in your details:
* `API_ID` and `API_HASH`: Obtained from [my.telegram.org](https://my.telegram.org)
* `HEDEF_GRUP`: The link of the target Telegram group (e.g., `[https://t.me/groupname](https://t.me/groupname)`)

5. **Run the script:**
```bash
python3 mesaj_silici.py
```

## ⚠️ Important Security Warning

This script uses Telethon, which generates a local `session_name.session` file to store your active Telegram login state. This file is **unencrypted** on your storage drive. 

Anyone with physical or background access to this specific `.session` file can potentially gain full access to your Telegram account without needing an SMS code or password. 
* Never upload or share your `.session` file.
* If you are running this script on a shared or remote machine, ensure you delete the `.session` file immediately after you are done.

## Disclaimer

This project is for educational purposes and personal message management only. Make sure to adhere to Telegram's Terms of Service and rate limits.
