from os import listdir
from os.path import isfile, join
from socket import *
import time
import json


def get_ip():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect(("255.255.255.255",50))
    ip,_ = sock.getsockname()
    newip = ip.split('.')
    newip = newip[0] + '.' + newip[1] + '.' + newip[2] + '.255'
    return newip


def get_json_data(files,username):
    d = {"username": username,
         "files":files}
    return json.dumps(d)


def announcer(ip, data):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    while True:
        sock.sendto(data.encode(), (ip,5000))
        time.sleep(60)  # 60 saniye bekletiyor.c


def wait_until(tick_time,count):
    temp = 0
    while True:
        temp = temp + tick_time
        if count*tick_time >= temp:
            break


if __name__ == "__main__":
    try:
        username = input("Enter a username : ")
        path = "host_files"
        files = [f for f in listdir(path) if isfile(join(path, f))]
        announcer('25.255.255.255', get_json_data(files, username)) #change
    except KeyboardInterrupt:
        print("Exit")