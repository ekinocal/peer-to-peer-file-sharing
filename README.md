Peer-to-Peer File Sharing Program
Tech
    Python3 - Socket programming
    NOTE: This program requires python-3.x to run.
    
How to Share Files?
Step 1: download the zipped file and extract it to the same directory. After that open
terminal and run these commands respectively.
python server.py
python service_announcer.py
python service_listener.py
python client.py
Optional: Windows users could simply double click .bat files. Optional: Run .py files
with IDE (such as PyCharm)
    In the Server side, write the name of the file you would like to share.
    Our program is going to divide that specified file into json chunks of five.
    In the service announcer please make sure that you write your nickname.
    Server Listener, lists the file name and nickname.
    Client, write the file that you would like to download to the console.
    Note: In order to share files between different computers, be sure to change
    get_ip() to server side and client side IPv4 address. You could change that at
    the line numbers as described below.
        After process is completed,
        user.txt has the nicknames saved.
        Logs files are as described below:
        date, time, ip address, chunkfile name
        i.e: 2020-05-10 15:55:19.136211,25.148.8.83,nickname_5
        Downloaded content is saved in the "downloads" folder.
Reference

These are reference links used: https://docs.python.org/3/library/json.html
https://docs.python.org/2/library/stringio.html https://stackabuse.com/reading-and-
writing-json-to-a-file-in-python/
