from os import kill, getpid
from time import sleep
from threading import Thread
import socket
import signal

global HOST, pid
# Use 127.0.0.1 for Private, 0.0.0.0 for Public
HOST = '0.0.0.0'
pid = getpid()
list_port=[]
min=0
max=0

def kill_process():
    print(f"\n{bcolors.RED}Closing process....{bcolors.ENDC}")
    if hasattr(signal, 'SIGKILL'):
        kill(pid, signal.SIGKILL)
    else:
        kill(pid, signal.SIGABRT)
    exit()

def open_port(port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        soc.bind((HOST, port))
        soc.listen(9)
        while 1:
            a,b = soc.accept()
            print(f"{bcolors.YELLOW}Port {port} | Accept: {b[0]}")
    except:
        pass

def start(list_port):
    print(f"\n{bcolors.YELLOW}- Starting spoof port...{bcolors.ENDC}")
    for port in list_port:
        try:
            Thread(target=open_port, args=(port,)).start()
        except KeyboardInterrupt:
            kill_process()
    while 1:
        try:
            print(f"{bcolors.ENDC}Keep spoof running...")
            sleep(500)
        except KeyboardInterrupt:
            kill_process()

if (__name__ == "__main__"):
    while 1:
        print(f"Use color? [Y/n]: ", end="")
        temp=str(input())
        if (temp == "Y") or (temp == "y"):
            class bcolors:
                BLUE = '\033[94m'
                CYAN = '\033[96m'
                GREEN = '\033[92m'
                YELLOW = '\033[93m'
                RED = '\033[91m'
                ENDC = '\033[0m'
            break
        elif (temp == "N") or (temp == "n"):
            class bcolors:
                BLUE = ''
                CYAN = ''
                GREEN = ''
                YELLOW = ''
                RED = ''
                ENDC = ''
            print('\033[0m',end="")
            break
    temp=str(input(f"\n{bcolors.YELLOW}1.{bcolors.CYAN} Min -> Max Port\n{bcolors.YELLOW}2. {bcolors.CYAN}Specify port\n {bcolors.GREEN}Choose: "))
    if (temp == "1"):
        while (min < 1) or (min > 65535):
            try:
                min=int(input(f"{bcolors.YELLOW}Min port: {bcolors.GREEN}"))
            except KeyboardInterrupt:
                kill_process()
            except:
                print(f"\n{bcolors.CYAN} Integer number [1-65535]\n First port while spoof\n{bcolors.ENDC}")
                min=0
        while (max < min) or (max > 65535):
            try:
                max=int(input(f"{bcolors.YELLOW}Max port: {bcolors.GREEN}"))
            except KeyboardInterrupt:
                kill_process()
            except:
                print(f"\n{bcolors.CYAN} Integer number [1-65535]\n Last port while spoof\n{bcolors.ENDC}")
                max=0
        for i in range(min,max+1,1):
            list_port.append(i)
    if (temp == "2"):
        list_port=[int(i) for i in input(f"\n{bcolors.YELLOW}Example: {bcolors.GREEN}22 80 443 3306 3389\n{bcolors.CYAN}Input port: {bcolors.GREEN}").split()]
    start(list_port)

