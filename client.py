#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


def main():
    sock = socket.socket()
    while True:

        sock.connect(('', 6677))
        message = input('Я: ')
        if not message:
            break
        sock.send(bytes(message, 'UTF-8'))

        data = sock.recv(1024)
        # print(data.decode('utf-8'))
        sock.close()

if __name__ == '__main__':
    main()