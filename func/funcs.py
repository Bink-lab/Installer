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
def download_file(game_name, filename, github_repo_url="https://github.com/Bink-lab/Sidneys-Installer", json_file_path="../games.json"):
    try:
        # Fetch game URLs from GitHub
        raw_url = f"{github_repo_url}/raw/main/{json_file_path}"
        response = requests.get(raw_url)
        data = response.json()
        game_urls = data.get("games", {}).get(game_name, [])
        
        # If URLs are found, proceed with downloading
        if game_urls:
            total_size = 0
            for i, url in enumerate(game_urls, start=1):
                try:
                    response = requests.get(url, stream=True)
                    total_size = int(response.headers.get('content-length', 0))
                    break
                except requests.exceptions.RequestException:
                    print(f"[ INFO ] Server {i} failed. Switching to the next server...")
                    continue

            if total_size == 0:
                print("[ ERROR ] Downloading failed.")
                return

            # Initialize progress bar
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=filename, ncols=100)

            with open(os.path.join("downloads", filename), 'wb') as file:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)
                    progress_bar.update(len(data))
            progress_bar.close()

            print(f"\n\n[ INFO ] File downloaded: {filename}")
            
        else:
            print("No URLs found for the specified game.")

    except Exception as e:
        print(f"An error occurred: {e}")

