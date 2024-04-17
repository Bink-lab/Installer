import requests
import os
import time
import wget
import keyboard
from termcolor import cprint, colored
from func.funcs import *

def github():
    # URL of the Github API
    url = "https://api.github.com/repos/bink-lab/Installer/releases/latest"

    try:
        # Get the release information
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        release = response.json()

        # Compare the tag name with the current version
        current_version = "2.23-Alpha"
        # Replace with the current version
        if release["tag_name"] > current_version:
            os.system("cls")
            watermark()
            cprint("[ INFO ] A new update is available! \n", 'white')
            # Find the asset with exe extension (self-installer)
            exe_asset = next((asset for asset in release["assets"] if asset["name"].endswith(".exe")), None)
            # Find the asset with zip extension (source code)
            zip_asset = next((asset for asset in release["assets"] if asset["name"].endswith(".zip")), None)
            if exe_asset and zip_asset:
                # Ask user for their choice
                cprint("[ INFO ] Choose the update type:\n", 'white')
                cprint("[1] Self-installer (exe)", 'white')
                cprint("[2] Source code (zip)", 'white')
                cprint("[3] Continue with current version", 'white')
                choice = input(colored("\n[ INFO ] Enter the number corresponding to your choice: ", 'white'))
                if choice == '1':
                    download_url = exe_asset['browser_download_url']
                elif choice == '2':
                    download_url = zip_asset['browser_download_url']
                elif choice == '3':
                    cprint("\n[ INFO ] Continuing with current version.", 'white')
                    return
                else:
                    cprint("\n[ ERROR ] Invalid choice. Exiting update process.", 'red')
                    return
                
                cprint(f"[ INFO ] Downloading the latest version from: {download_url}\n", 'white')
                quote()
                filename = wget.download(download_url)
                os.system("cls")
                watermark()
                cprint(f"\n\n[ Update downloaded: {filename} ]\n", 'white')
                cprint("[ INFO ] Use the new version!", 'white')
                cprint("[ INFO ] Opening download directory...", 'white')
                time.sleep(2)  # Wait for a moment before opening the directory
                directory = os.path.dirname(os.path.realpath(filename))
                subprocess.Popen(f'explorer "{directory}"')  # Open directory in file explorer
                cprint("[ INFO ] Press 'esc' to exit", 'white')
                keyboard.wait("esc")
                exit()
            else:
                cprint("\n[ ERROR ] Could not find both exe and zip files for this update.", 'red')
        else:
            cprint("\n[ INFO ] Current version is up-to-date.", 'white')
    except requests.RequestException as e:
        cprint("\n[ ERROR ] Error fetching release information:", 'red')
        cprint(str(e), 'red')
        time.sleep(2)