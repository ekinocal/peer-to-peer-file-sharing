import socket
import os
import time
import math
import json
from threading import *
from datetime import *


def write_log(log_file, message):
    with open("logs/"+log_file,"a") as file:
        file.write(str(datetime.now()) + "," + message)


def get_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("255.255.255.255",5))
    ip = sock.getsockname()[0]
    return ip


def divide_into_chunks(file, fileName, directory):   ##server
    if not os.path.exists(directory):
        os.makedirs(directory)
    c = os.path.getsize(file)
    CHUNK_SIZE = math.ceil(math.ceil(c) / 5)
    cnt = 1
    with open(file, 'rb') as infile:
        divided_file = infile.read(int(CHUNK_SIZE))
        while divided_file:
            name = directory + "/" + fileName.split('.')[0] + "_" + str(cnt)
            with open(name, 'wb+') as div:
                div.write(divided_file)
            cnt += 1
            divided_file = infile.read(int(CHUNK_SIZE))

def server_start(ip):
    print("ip : " + ip)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip,5001))
    sock.listen(10)
    while True:
        conn, info = sock.accept()
        Thread(target=process_connection,args=(conn,info)).start()


def process_connection(conn,info):
    while True:
        try:
            message = conn.recv(4096)
            if len(message) == 0:
                break
            message = json.loads(message.decode())["filename"]
            with open("host_files/" + message, "rb") as chunk_file:
                conn.send(chunk_file.read())
                write_log("server_success.log", message + "," + info[0]) # i think we're done here.
        except:
            write_log("server_fail.log","Error on sending file to client.")
            break
        finally:
            conn.close()



if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.makedirs("logs")
    path = input("Enter file path or name(if it is on same directory) : ")
    fileName = path.split('/')[len(path.split('/'))-1].split('.')[0]
    divide_into_chunks(path,fileName,"host_files")
    server_start('25.93.121.169') #get ipler degisti