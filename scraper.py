import random
import requests
from colorama import *
import threading

def scrape_group():
    id = random.randint(1111111, 9999999)
    r = requests.get(f"https://groups.roblox.com/v2/groups?groupIds={id}")
    if r.status_code == 200:
        try:
            data = r.json()
            extracted_data = {
                'id': data['data'][0]['id'],
                'name': data['data'][0]['name'],
                'hasVerifiedBadge': data['data'][0]['hasVerifiedBadge']
            }
            ln = extracted_data['name'].replace(' ', '-')
            link = f"https://www.roblox.com/groups/{extracted_data['id']}/{ln}#!/about"
            print(f"{Fore.GREEN}Scraped Successfully {Fore.RESET}| {Fore.GREEN}Name:[{extracted_data['name']}] {Fore.RESET}| {Fore.GREEN}Link:[{link}] {Fore.RESET}| {Fore.GREEN}VerifiedBadge:[{extracted_data['hasVerifiedBadge']}] {Fore.RESET}| {Fore.GREEN}ID:[{extracted_data['id']}]")
            with open("groups.txt", "a") as f:
                f.write(f"{link}\n")
        except Exception as e:
            print(F"{Fore.RED}Scrape Failed:", e)

def scrape_loop():
    for _ in range(1000000000000000000000000000000000000000000):
        scrape_group()
        print("made by ltcflip")

num_threads = 10

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=scrape_loop)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
