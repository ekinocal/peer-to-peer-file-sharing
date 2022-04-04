from socket import *
import json
import platform

files_dictionary = {}

class User:
    username = ""
    ip = ""
    def __init__(self,ip,username):
        self.ip = ip
        self.username = username

def get_ip():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect(("255.255.255.255",50))
    ip,_ = sock.getsockname()
    newip = ip.split('.')
    newip = newip[0] + '.' + newip[1] + '.' + newip[2] + '.255' if platform.system() != "Windows" else ip

    return newip


def start_listener_server(ip):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((ip,5000))

    while True:
        message, address = sock.recvfrom(4096)
        ip, _ = address
        x = json.loads(message.decode())
        for file in x["files"]:
            user = User(ip,x["username"])
            if not file in files_dictionary:
                files_dictionary[file] = []
            is_found = False
            for data in files_dictionary[file]:
                if data.username == x["username"] and data.ip == ip:
                    is_found = True
            if not is_found:
                files_dictionary[file].insert(0, user)
        with open("users.txt","w") as user_file:
            for key in files_dictionary:
                for file_info in files_dictionary[key]:
                    user_file.write(file_info.username + "," + file_info.ip + "," + key + "\n")


if __name__ == '__main__':
    try:
        start_listener_server('25.93.121.169') #hamachi icin degistiriliyor
    except KeyboardInterrupt:
        print("Exit")