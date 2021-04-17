import requests
import threading
import json

def send_report(token, guild, channel, message):
    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        payload = { 
            'channel_id': channel,
            'guild_id': guild,
            'message_id': message,
            'reason': "1"
        }
        requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)

def print_banner():
    banner = r"""
  __  __               _____                       _   
 |  \/  |             |  __ \                     | |  
 | \  / | __ _ ___ ___| |__) |___ _ __   ___  _ __| |_ 
 | |\/| |/ _` / __/ __|  _  // _ \ '_ \ / _ \| '__| __|
 | |  | | (_| \__ \__ \ | \ \  __/ |_) | (_) | |  | |_ 
 |_|  |_|\__,_|___/___/_|  \_\___| .__/ \___/|_|   \__|
                                 | |                   
                                 |_|         
                    V1 Made By Echo              
    """
    print(banner)

def setup():
    print_banner()
    target_token = input("Enter target token: ")
    target_guild = input("Enter guild id: ")
    target_channel = input("Enter target channel id: ")
    target_message = input("Enter target message id: ")
    threads_amount = input("Enter the amount of threads: ")
    thread = threading.Thread(target=send_report, args=[target_token,target_guild,target_channel,target_message])
    for x in range(int(threads_amount)):
        thread.start()
        print("Started thread number: " + x)

setup()
