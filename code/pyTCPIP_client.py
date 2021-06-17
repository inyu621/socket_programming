# -*- coding: utf-8 -*-

from socket import *
import select as sel
import sys 
  
sock = socket(AF_INET, SOCK_STREAM) 
if len(sys.argv) != 3: # 인자 값이 부족할 때
    print("How to use : python3 pyTCPIP_client.py [IP] [PORT]")
    exit()
IP = str(sys.argv[1]) # 첫번째 인자 값을 IP주소로 받음
PORT = int(sys.argv[2]) # 두번째 인자 값을 PORT번호로 받음
sock.connect((IP, PORT)) 
  
while True: 
    streamlist = [sys.stdin, sock] # 입력 스트림 목록 유지 리스트

    read_sockets, write_socket, error_socket = sel.select(streamlist,[],[]) 
  
    for socks in read_sockets: 
        if socks == sock: 
            msg = socks.recv(4096) 
            print(msg) 
        else: 
            msg = sys.stdin.readline() 
            sock.send(msg) 
            sys.stdout.write("[ Me ]") 
            sys.stdout.write(msg) 
            sys.stdout.flush() 

server.close() 
