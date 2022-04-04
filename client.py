import socket
import sys
import os
import logging
from datetime import datetime
import time
import json

global_file_dicts = {}

class File:
    username = ""
    file_name = ""
    ip_address = ""
    def __init__(self,username,file_name,ip_address):
        self.username = username
        self.file_name = file_name
        self.ip_address = ip_address


def parse_users():
    with open("users.txt","r") as file:
        lines = file.readlines()
        for x in lines:
            args = x.split(',')
            file = File(args[0],args[2].strip()[:-2],args[1])
            if file.file_name in global_file_dicts:
                flag = True
                for a in global_file_dicts[file.file_name]:
                    if a.ip_address == file.ip_address and a.username == file.username:
                        flag = False
                if flag:
                    global_file_dicts[file.file_name].insert(0,file)
            else:
                global_file_dicts[file.file_name] = [file]


def print_menu():
    for x in global_file_dicts:
        for arr in global_file_dicts[x]:
            print("Username : " + arr.username + " File Name : " + arr.file_name + " IP Address : " + arr.ip_address)
    file_input = input("Enter a file_name")
    for x in range(1,6):
        file = global_file_dicts[file_input][0]
        get_file(file.ip_address, file.file_name + "_" + str(x))
    combine_chunks(file_input,'.',"downloads")


def log(file_name, message):
    with open(file_name,"w") as file:
        file.write(str(datetime.now()) + "," + message)


def get_file(ip,file_name):
    print("IP : " + ip + " File Name : " + file_name)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,5001))
    try:
        sock.send(json.dumps({"filename": file_name}).encode())
        while True:
            data = sock.recv(4096)
            if  len(data) == 0:
                log("client_success.log", ip+","+file_name)
                break
            with open(file_name, "ab") as file:
                file.write(data)
    except:
        log("client_fail.log", ip + "," + file_name)

    finally:
        sock.close()

def combine_chunks(inp,sourcedir,outputdir):
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    with open(outputdir + '/' + inp, 'wb') as outfile:
        for i in range(1, 6):
            with open(sourcedir + '/'+inp + "_" + str(i), "rb") as infile:
                outfile.write(infile.read())
    for i in range(1, 6):
        if os.path.exists(inp + "_" + str(i)):
            os.remove(inp + "_" + str(i))


if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs("downloads")
    while True:
        parse_users()
        print_menu()



