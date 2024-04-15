import wget
import os
import keyboard
import time
import requests
from termcolor import colored, cprint
import subprocess
from func.funcs import *

# VERGEET NIET DE NIEUWE VERSIE TE NOEMEN

# Autoclicker
file_to_run = "/apps/main.exe"

def esc():
    print("\n[ Druk op 'esc' om te stoppen ]")
    keyboard.wait("esc")
    exit()
    


# Maak de map 'downloads' aan als deze niet bestaat
if not os.path.exists("downloads"):
    os.makedirs("downloads")

def custom():
    # Vraag de gebruiker om een link te geven
    url = input("\n[ Directe link ] : ")

    # Maak de map 'downloads' aan als deze niet bestaat
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    filename = wget.download(url, out="downloads")

    cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
    time.sleep(2)
    shortcuts()

def shortcuts():
    import os
    os.system("cls")
    watermark()
    cprint("\n\n[ Shortcuts ]\n", 'light_red')
    cprint("[01] Roblox" , 'white')
    cprint("[02] Opera GX [ Nieuwste ]", 'white')
    cprint("[03] Discord [ Ouder ]", 'white')
    cprint("[04] Minecraft [ Cracked SKLauncher ]", 'light_red')
    cprint("[05] Skype [ Nieuwste ]", 'white')
    cprint("[06] Autoclicker [ Custom ]", 'white')
    cprint("[07] Macro", 'white')
    cprint("[08] Games [ Binnenkort 😈 ]", 'light_red')
    cprint("\n[0] Eigen", 'light_red')

    nummer = input(colored("\n[ Shortcut ] : ", 'white'))
    if nummer == "01":
            os.system("cls")
            watermark()
            cprint(f"\n[ Roblox ]", 'white')
            cprint(f"\n\n[01] Roblox Player", 'white')
            cprint(f"[02] Roblox Fps Unlocker [ Altijd Nieuwste ]", 'white')
            cprint(f"\n[0] Terug", 'white')
            roblox = input(colored("\n[ Nummer ] : ", 'white'))
            os.system("cls")
            watermark()
            if roblox == "01":
                url = "http://setup.rbxcdn.com/Roblox.exe"
                filename = wget.download(url, out="downloads")
                cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
                time.sleep(2)
                shortcuts()
            if roblox == "02":
                url = "https://github.com/axstin/rbxfpsunlocker/releases/download/v5.2/rbxfpsunlocker-x64.zip"
                filename = wget.download(url, out="downloads")
                cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
                time.sleep(2)
                shortcuts()

            if roblox == "0":
                shortcuts()
            else:
                exit()


            cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
            time.sleep(2)
            shortcuts()

    if nummer == "02":
        os.system("cls")
        watermark()
        url = "https://files1.majorgeeks.com/10afebdbffcd4742c81a3cb0f6ce4092156b4375/browsers/OperaGXPortable_107.0.5045.60.paf.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
        time.sleep(2)
        shortcuts()

    if nummer == "03":
        os.system("cls")
        watermark()
        url = "https://github.com/portapps/discord-portable/releases/download/1.0.9028-17/discord-portable-win32-1.0.9028-17-setup.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
        time.sleep(2)
        shortcuts()

    if nummer == "04":
        os.system("cls")
        watermark()
        cprint(f"\n[ INFO ] Minecraft werkt op het moment niet, wacht tot een latere update.", 'white')
        time.sleep(3)
        shortcuts()

    if nummer == "05":
        os.system("cls")
        watermark()
        url = "https://github.com/portapps/skype-portable/releases/download/8.110.0.218-97/skype-portable-win32-8.110.0.218-97-setup.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
        time.sleep(2)
        shortcuts()
    
    if nummer == "06":
        os.system("cls")
        watermark()
        url = "https://github.com/Bink-lab/Installer/raw/main/Components/autoclicker.exe"
        filename = wget.download(url, out="downloads")
        cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
        time.sleep(2)
        shortcuts()
    if nummer == "07":
        os.system("cls")
        watermark()
        cprint(f"\n\n[ Macro ]", 'white')
        cprint(f"\n[01] TG Macro", 'white')
        cprint(f"\n[0] Terug", 'white')
        macro = input("\n[ Nummer ] : ")
        if macro == "01":
            os.system("cls")
            watermark()
            url = "https://tgmacro.org/portable.zip"
            filename = wget.download(url, out="downloads")
            cprint(f"\n\n[ INFO ] Bestand gedownload: {filename}", 'white')
            time.sleep(2)
            shortcuts()
        if macro == "0":
            shortcuts()

    if nummer == "0":
        os.system("cls")
        watermark()
        custom()
    
    else:
        os.system("cls")
        watermark()
        cprint("\n[ INFO ] Geen geldige optie", 'white')
        time.sleep(1)
        os.system("cls")
        shortcuts()


def udc():
# Controleer op updates
    os.system("cls")
    watermark2()
    cprint("\n[ INFO ] Controleren op updates... ]", 'white')
    github()
    shortcuts()
udc()

# Menu
shortcuts()