from os import system as c
import time
import random

# Colour
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'

# Banner
def logo():
    c("clear")
    print(f"""{G}
██╗  ██╗ ██████╗ ███╗   ██╗██╗ ██████╗███████╗
██║  ██║██╔═══██╗████╗  ██║██║██╔════╝██╔════╝
███████║██║   ██║██╔██╗ ██║██║██║     █████╗  
██╔══██║██║   ██║██║╚██╗██║██║██║     ██╔══╝  
██║  ██║╚██████╔╝██║ ╚████║██║╚██████╗███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝
{Y}       HACKING WORLD - HGNICE AVIATOR TOOL
{A}------------------------------------------------
""")

# Progress animation
def progress(task):
    for i in range(1, 21):
        print(f"{C}[{G}{'='*i}{' '*(20-i)}] {i*5}% {Y}{task}", end='\r')
        time.sleep(0.15)
    print()

# Main work
def connect_uid():
    logo()
    uid = input(f"{C}ENTER YOUR HGNICE UID: ")
    print(f"{Y}[+] Connecting to HGNICE Aviator Server for UID: {uid}...\n")
    time.sleep(2)
    progress("Verifying UID")
    print(f"{G}[✓] UID Verified Successfully!\n")
    time.sleep(1)
    print(f"{Y}[+] Checking Credit Balance...")
    time.sleep(2)
    print(f"{R}[X] 409৳ CREDIT NOT FOUND!\n")
    print(f"{Y}👉 Please Purchase {G}409৳ Credit{Y} to Activate Hack Feature.\n")
    print(f"{A}Contact Support: https://your-panel-link.com\n")
    input(f"{A}Press Enter to Exit...")

# Menu
def menu():
    logo()
    print(f"{A}[1] Start UID Connection")
    print(f"{A}[0] Exit Tool")
    print(f"{A}-----------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        connect_uid()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()