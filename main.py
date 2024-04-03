import requests
import random
import time
import os
from colorama import Fore

print("=============================================\n")
print("──────████─█───█─████─█──█─███─████─█──█─────")
print("──────█──█─██─██─█──█─██─█─█───█──█─█─█──────")
print("──────████─█─█─█─████─█─██─███─█────██───────")
print("──────█──█─█───█─█──█─█──█─█───█──█─█─█──────")
print("──────█──█─█───█─█──█─█──█─███─████─█──█─────\n")
print("=============================================")
print("─████─████─█───█─█───█─█─█─█──█─███─███─██─██")
print("─█──█─█──█─██─██─██─██─█─█─██─█──█───█───███─")
print("─█────█──█─█─█─█─█─█─█─█─█─█─██──█───█────█──")
print("─█──█─█──█─█───█─█───█─█─█─█──█──█───█────█──")
print("─████─████─█───█─█───█─███─█──█─███──█────█──\n")
print("=============================================")

author = "Amaneck Community"
print("Author: " + author)
script = "AutoPost Discord"
print("Script: " + script)
discord = "https://dsc.gg/amaneckcps"
print("Discord: " + discord)
print("===========================================")
print('         WARNING: DONT SHARE FILE'          )
print("===========================================\n")

time.sleep(1)

channel_id = input("Enter the channel ID: ")
waktu2 = int(input("time to send the message (second): "))

time.sleep(1)
print("Run through 3")
time.sleep(1)
print("Run through 2")
time.sleep(1)
print("Run through 1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("message.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(words).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break

        time.sleep(waktu2)
