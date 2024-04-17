import time
import requests
import wget
import subprocess
import os
import keyboard
from termcolor import colored, cprint
from func.api.quotes_api import quote

def watermark2():
    print(colored(f"""$$$$$$$\  $$\           $$\               $$\                $$\       
$$  __$$\ \__|          $$ |              $$ |               $$ |      
$$ |  $$ |$$\ $$$$$$$\  $$ |  $$\         $$ |      $$$$$$\  $$$$$$$\  
$$$$$$$\ |$$ |$$  __$$\ $$ | $$  |$$$$$$\ $$ |      \____$$\ $$  __$$\ 
$$  __$$\ $$ |$$ |  $$ |$$$$$$  / \______|$$ |      $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$ |$$ |  $$ |$$  _$$<          $$ |     $$  __$$ |$$ |  $$ |
$$$$$$$  |$$ |$$ |  $$ |$$ | \$$\         $$$$$$$$\\$$$$$$$ |$$$$$$$  |
\_______/ \__|\__|  \__|\__|  \__|        \________|\_______|\_______/ 
                                                                       
                                                                       
                                                                       \n\n""", 'white'))
    quote()
    time.sleep(2)

def watermark():
    print(colored(f"""$$$$$$$\  $$\           $$\               $$\                $$\       
$$  __$$\ \__|          $$ |              $$ |               $$ |      
$$ |  $$ |$$\ $$$$$$$\  $$ |  $$\         $$ |      $$$$$$\  $$$$$$$\  
$$$$$$$\ |$$ |$$  __$$\ $$ | $$  |$$$$$$\ $$ |      \____$$\ $$  __$$\ 
$$  __$$\ $$ |$$ |  $$ |$$$$$$  / \______|$$ |      $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$ |$$ |  $$ |$$  _$$<          $$ |     $$  __$$ |$$ |  $$ |
$$$$$$$  |$$ |$$ |  $$ |$$ | \$$\         $$$$$$$$\\$$$$$$$ |$$$$$$$  |
\_______/ \__|\__|  \__|\__|  \__|        \________|\_______|\_______/ 
                                                                       
                                                                       
                                                                       \n\n""", 'white'))

from tqdm import tqdm


# Function to download file from URL and save it with the correct name
def download_file(url_list, filename):
    total_size = 0

    # Try each URL until one succeeds
    for i, url in enumerate(url_list, start=1):
        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            break
        except requests.exceptions.RequestException:
            cprint(f"[ INFO ] Server {i} failed, Switching to the next server...", 'white')
            cprint(f"\n[ INFO ] Connecting to Server {i}...\n", 'white')
            time.sleep(1)
            continue

    if total_size == 0:
        os.system("cls")
        watermark()
        cprint("[ ERROR ] Downloading failed.", 'white', filename)
        return

    # Initialize progress bar
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=filename, ncols=100)

    with open(os.path.join("downloads", filename), 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            progress_bar.update(len(data))
    progress_bar.close()
    cprint(f"\n\n[ INFO ] File downloaded: {filename}", 'white')
    time.sleep(5)






