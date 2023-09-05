#!/usr/bin/env python3

import socket

HOST = socket.gethostbyname("koukoku.shadan.open.ad.jp")
PORT = 23
BUFSIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while 1:
    data = client.recv(BUFSIZE)
    if len(data) == 0:
        break
    print(data.decode("shift_jis"), end="", flush=True)
client.close()
