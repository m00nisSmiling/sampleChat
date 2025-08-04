import socket
import threading
import os
from termcolor import colored

os.system("clear")
os.system("cat ./cache.log")
print(colored("                      --------- ","blue"))
print(colored("                     <CHAT CLIENT>","red"))
print(colored("                      --------- ","blue"))

os.system("ip a | grep 192.168 | cut -d '/' -f1")
HOST = input(colored("    [!] Host Ip : ","magenta"))
PORT = 12345

def handle_receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(colored("\n<- ","blue"),f"{data.decode()}\n-> ", end="")
            fileo = open("./cache.log",'a')
            fileo.write(f"\n<- {data.decode()}")
            fileo.close()
        except:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(colored("[+] Connected to server!","green"))
fileo = open("./cache.log",'a')
fileo.write("\n[+] Connected to server!")
fileo.close()
threading.Thread(target=handle_receive, args=(client_socket,), daemon=True).start()

try:
    while True:
        msg = input("-> ")
        fileo = open("./cache.log",'a')
        fileo.write(f"\n-> {msg}")
        fileo.close()
        client_socket.sendall(msg.encode())
except KeyboardInterrupt:
    print(colored("\n[!] Chat ended.","red"))
    fileo = open("./cache.log",'a')
    fileo.write("\n[!] Chat ended.\n")
    fileo.close()
finally:
    client_socket.close()
