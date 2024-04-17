import wget
import os
import keyboard
import time
import requests
from termcolor import colored, cprint
import subprocess
from func.funcs import *
from func.api.update import *

# REMEMBER TO NAME THE NEW VERSION

# Create the 'downloads' folder if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")

def open_subfolder(subfolder_name):
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the subfolder
    subfolder_path = os.path.join(current_directory, subfolder_name)
    
    try:
        # Open the subfolder in file explorer
        subprocess.Popen(['explorer', subfolder_path], shell=True)
    except OSError:
        print(f"Subfolder '{subfolder_name}' not found.")

# Example usage:
subfolder_name = "downloads"  # Adjusted to match the subfolder name

# Autoclicker
file_to_run = "/apps/main.exe"

def custom():
    try:
        # Ask the user to provide a link
        url = input(colored("\n[ Direct link ] : ", 'white'))

        filename = wget.download(url, out="downloads")

        cprint(f"\n\n[ INFO ] File downloaded: {filename}", 'white')
        time.sleep(2)
        shortcuts()
    except Exception as e:
        # Handle the error gracefully
        cprint(f"\n[ ERROR ] An error occurred during the download: {e}", ' white')
        # Optionally, you can log the error, display a user-friendly message, or attempt to recover


def shortcuts():
    import os
    os.system("cls")
    watermark()

    # Define colors
    color_normal = 'white'
    color_broken = 'light_red'
    color_unfinished = 'light_yellow'
    
    # Print border and title
    cprint("╔══════════════════════════════════════════════════╗", color_normal)
    cprint("║                   Shortcuts                      ║", color_normal)
    cprint("╠══════════════════════════════════════════════════╣", color_normal)
    
    # Print options
    cprint("║ [01] Roblox" , color_normal)
    cprint("║ [02] Opera GX", color_normal)
    cprint("║ [03] Discord", color_normal)
    cprint("║ [04] Minecraft [ Titan Launcher, Unfinished ]", color_unfinished)
    cprint("║ [05] Skype", color_normal)
    cprint("║ [06] Autoclicker [ Unfinished ]", color_unfinished)
    cprint("║ [07] Macro", color_normal)
    cprint("║ [08] Games [ Unfinished ]", color_unfinished)
    cprint("║", color_normal)
    cprint("║ [0] Custom", color_normal)
    cprint("║", color_normal)
    cprint("║ [00] Open Download Folder", color_normal)
    
    # Print bottom border
    cprint("╚══════════════════════════════════════════════════╝", color_normal)


    nummer = input(colored("\n[ Number ] : ", 'white'))
    if nummer == "01":
        os.system("cls")
        watermark()
        print("╔══════════════════════════════════════════════════╗")
        cprint("║                   Roblox                         ║", color_normal)
        print("╠══════════════════════════════════════════════════╣")
        cprint("║ [01] Roblox Player", color_normal)
        cprint("║ [02] Roblox Fps Unlocker [ Always Latest ]", color_normal)
        cprint("║", color_normal)
        cprint("║ [0] Back", color_normal)
        print("╚══════════════════════════════════════════════════╝")
        roblox = input(colored("\n[ Number ] : ", color_normal))
        os.system("cls")
        watermark()
        if roblox == "01":
            url = "http://setup.rbxcdn.com/Roblox.exe"
            filename = wget.download(url, out="downloads")
            cprint(f"\n\n[ INFO ] File downloaded: {filename}", color_normal)
            time.sleep(2)
            shortcuts()
        elif roblox == "02":
            url = "https://github.com/axstin/rbxfpsunlocker/releases/download/v5.2/rbxfpsunlocker-x64.zip"
            filename = wget.download(url, out="downloads")
            cprint(f"\n\n[ INFO ] File downloaded: {filename}", color_normal)
            time.sleep(2)
            shortcuts()
        elif roblox == "0":
            shortcuts()


    if nummer == "02":
        os.system("cls")
        watermark()
        url = "https://files1.majorgeeks.com/10afebdbffcd4742c81a3cb0f6ce4092156b4375/browsers/OperaGXPortable_107.0.5045.60.paf.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] File downloaded: {filename}", 'white')
        time.sleep(2)
        shortcuts()

    if nummer == "03":
        os.system("cls")
        watermark()
        url = "https://github.com/portapps/discord-portable/releases/download/1.0.9028-17/discord-portable-win32-1.0.9028-17-setup.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] File downloaded: {filename}", 'white')
        time.sleep(2)
        shortcuts()

    if nummer == "04":
        os.system("cls")
        watermark()
        url = "https://git-link.vercel.app/api/download?url=https%3A%2F%2Fgithub.com%2FBink-lab%2Fshortcuts%2Fblob%2Fmain%2FMinecraft-Launcher.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] File downloaded: TitanLauncher.exe", 'white')
        time.sleep(2)
        shortcuts()

    if nummer == "05":
        os.system("cls")
        watermark()
        url = "https://github.com/portapps/skype-portable/releases/download/8.110.0.218-97/skype-portable-win32-8.110.0.218-97-setup.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] File downloaded: {filename}", 'white')
        time.sleep(2)
        shortcuts()
    
    if nummer == "06":
        os.system("cls")
        watermark()
        url = "https://github.com/Bink-lab/Installer/raw/main/Components/autoclicker.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] File downloaded: {filename}", 'white')
        time.sleep(2)
        shortcuts()
        
    if nummer == "07":
        os.system("cls")
        watermark()
        print("╔══════════════════════════════════════════════════╗", color_normal)
        cprint("║                   Macro                          ║", color_normal)
        cprint("╠══════════════════════════════════════════════════╣", color_normal)
        cprint("║ [01] TG Macro", color_normal)
        cprint("║", color_normal)
        cprint("║ [0] Back", color_normal)
        print("╚══════════════════════════════════════════════════╝", color_normal)
        macro = input("\n[ Number ] : ")
        if macro == "01":
            os.system("cls")
            watermark()
            url = "https://tgmacro.org/portable.zip"
            filename = wget.download(url, out="downloads")
            cprint(f"\n\n[ INFO ] File downloaded: {filename}", color_normal)
            time.sleep(2)
            shortcuts()
        elif macro == "0":
            shortcuts()
            
    if nummer == "08":
        os.system("cls")
        watermark()
        cprint("╔══════════════════════════════════════════════════╗", color_normal)
        cprint("║                   Games                         ║", color_normal)
        cprint("╠══════════════════════════════════════════════════╣", color_normal)
        cprint("║ [01] 'Bloons TD 6' [ Dual Servers ]", color_normal)
        cprint("║ [02] 'Thats not my neighbor' [ Dual Servers ] ", color_normal)
        cprint("║ [03] 'Grand Theft Auto - San Andreas' [ Dual Servers ] [ Might not work on pc's w/o administrator ] ", color_normal)
        cprint("║", color_normal)
        cprint("║ [0] Back", color_normal)
        cprint("╚══════════════════════════════════════════════════╝")
        games = input(colored("\n[ Number ] : ", color_normal))
        os.system("cls")
        watermark()
        if games == "01":
            os.system("cls")
            watermark()
            url_list = ["https://dl.bzzhr.co/1780649439596244992", "https://dl.buzzheavier.com/1780612802420314112"]  # Replace with actual URLs
            download_file(url_list, "Bloons-TD-6.zip")
            shortcuts()
        elif games == "02":
            os.system("cls")
            watermark()
            url_list = ["https://dl.bzzhr.co/1780647335431368704", "https://dl.buzzheavier.com/1780650490968051712"]  # Replace with actual URLs
            download_file(url_list, "Thats-Not-My-Neighbor.zip")
            shortcuts()
        elif games == "03":
            os.system("cls")
            watermark()
            url_list = ["https://dl.bzzhr.co/1780652785249939456", "https://dl.buzzheavier.com/1780652804877488128"]  # Replace with actual URLs
            download_file(url_list, "Grand-Theft-Auto-San-Andreas.zip")
            shortcuts()
        elif games == "0":
            shortcuts()

    if nummer == "00":
        os.system("cls")
        # Code to open the directory
        directory = os.path.join(os.getcwd(), "downloads")  # Get the path to the "downloads" directory
        subprocess.Popen(f'explorer "{directory}"')  # Open directory in file explorer
        shortcuts()
    
    if nummer == "0":
        os.system("cls")
        watermark()
        custom()
    
    else:
        os.system("cls")
        watermark()
        cprint("\n[ INFO ] Invalid option", 'white')
        time.sleep(1)
        os.system("cls")
        shortcuts()

def udc():
    # Check for updates
    os.system("cls")
    watermark2()
    cprint("\n[ INFO ] Checking for updates... ]", 'white')
    github()
    shortcuts()

#udc()
shortcuts()