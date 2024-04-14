import time
import requests
import wget
import os
import keyboard
from termcolor import colored, cprint
from func.api.quotes_api import quote

def watermark2():
    print(colored(f"""$$$$\        $$$$$$\  $$\       $$\                                     $$$$\ 
$$  _|      $$  __$$\ \__|      $$ |                                    \_$$ |
$$ |        $$ /  \__|$$\  $$$$$$$ |$$$$$$$\   $$$$$$\  $$\   $$\         $$ |
$$ |        \$$$$$$\  $$ |$$  __$$ |$$  __$$\ $$  __$$\ $$ |  $$ |        $$ |
$$ |         \____$$\ $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |        $$ |
$$ |        $$\   $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |        $$ |
$$$$\       \$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |      $$$$ |
\____|       \______/ \__| \_______|\__|  \__| \_______| \____$$ |      \____|
                                                        $$\   $$ |            
                                                        \$$$$$$  |            
                                                         \______/             \n\n""", 'white'))
    quote()
    time.sleep(2)

def watermark():
    print(colored(f"""$$$$\        $$$$$$\  $$\       $$\                                     $$$$\ 
$$  _|      $$  __$$\ \__|      $$ |                                    \_$$ |
$$ |        $$ /  \__|$$\  $$$$$$$ |$$$$$$$\   $$$$$$\  $$\   $$\         $$ |
$$ |        \$$$$$$\  $$ |$$  __$$ |$$  __$$\ $$  __$$\ $$ |  $$ |        $$ |
$$ |         \____$$\ $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |        $$ |
$$ |        $$\   $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |        $$ |
$$$$\       \$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |      $$$$ |
\____|       \______/ \__| \_______|\__|  \__| \_______| \____$$ |      \____|
                                                        $$\   $$ |            
                                                        \$$$$$$  |            
                                                         \______/             \n\n""", 'white'))

def github():
    # URL van de Github API
    url = "https://api.github.com/repos/bink-lab/Installer/releases/latest"

    try:
        # Haal de release informatie
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        release = response.json()

        # Vergelijk de tagnaam met de huidige versie
        current_version = "2.12-Alpha"
        # Vervang met de huidige versie
        if release["tag_name"] > current_version:
            cprint("[ INFO ] Er is een nieuwe update beschikbaar! \n", 'white')
            cprint("[ INFO ] Download de nieuwste versie: ", release["assets"][0]["browser_download_url"], " \n", 'white')
            quote()
            filename = wget.download(release["assets"][0]["browser_download_url"])
            cprint(f"\n\n[ Update gedownload: {filename} ]\n", 'white')
            cprint("[ INFO ] Gebruik de nieuwe versie!", 'white')
            cprint("[ INFO ] Druk op 'esc' om te stoppen", 'white')
            keyboard.wait("esc")
            exit()
        else:
            cprint("\n[ INFO ] Huidige versie is up-to-date.", 'white')
    except requests.RequestException as e:
        cprint("\n[ ERROR ] Fout bij het ophalen van release informatie:", 'red')
        cprint(str(e), 'red')
        time.sleep(2)



