import os
import time
import sys
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
from dotenv import load_dotenv

load_dotenv()

API_ID_STR = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
HEDEF_GRUP = os.getenv('HEDEF_GRUP')

if not API_ID_STR or not API_HASH or not HEDEF_GRUP:
    raise ValueError("Error: API_ID, API_HASH, or HEDEF_GRUP is missing in the .env file.")

API_ID = int(API_ID_STR)

print(f"Target Group: {HEDEF_GRUP}")
confirmation = input("WARNING: Your messages in this group will be permanently deleted for everyone. Do you want to continue? (y/n): ")

if confirmation.lower() != 'y':
    print("Operation cancelled.")
    sys.exit()

print("Connecting to Telegram...")

with TelegramClient('session_name', API_ID, API_HASH) as client:
    print("Connected. Fetching messages...")
    
    deleted_count = 0
    
    for message in client.iter_messages(HEDEF_GRUP, from_user='me'):
        try:
            preview = message.text[:30] if message.text else 'Media/Other'
            print(f"Deleting: {preview}...") 
            
            client.delete_messages(HEDEF_GRUP, message.id, revoke=True)
            deleted_count += 1
            
            time.sleep(2)
            
        except FloodWaitError as e:
            print(f"Rate limit reached. Sleeping for {e.seconds} seconds to prevent ban...")
            time.sleep(e.seconds)
        except Exception as e:
            print(f"Error: {e}")

    print(f"\nDone! Total {deleted_count} messages deleted.")