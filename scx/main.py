import socket
import threading
import os
from termcolor import colored

os.system("clear")
os.system("cat ./cache.log")
print(colored("			        --------- ","blue"))
print(colored("			       <CHAT HOST>","red"))
print(colored("				--------- ","blue"))

os.system("ip a | grep 192.168 | cut -d '/' -f1")

HOST = '0.0.0.0'
PORT = 12345

def handle_receive(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(colored("\n<- ","blue"),f"{data.decode()}\n-> ", end="")
            fileo = open("./cache.log",'a')
            fileo.write(f"\n<- {data.decode()}")
            fileo.close()
        except:
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(colored("    [+] PORT ","magenta"),colored(f"{PORT}...","blue"))

conn, addr = server_socket.accept()
print(f"[+] Connected ip : {addr}")
fileo = open("./cache.log","a")
fileo.write(f"\n[+] Connected ip : {addr}")
fileo.close()
threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()

try:
    while True:
        msg = input("-> ")
        fileo = open("./cache.log","a")
        fileo.write(f"\n-> {msg}")
        fileo.close()
        conn.sendall(msg.encode())
except KeyboardInterrupt:
    print("\n[!] SESSION CLOSED.")
    fileo = open("./cache.log","a")
    fileo.write("\n[!] SESSION CLOSED.\n")
    fileo.close()
finally:
    conn.close()
    server_socket.close()
