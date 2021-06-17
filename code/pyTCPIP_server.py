from socket import *
from _thread import *
import select 
import sys 
  
sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  
if len(sys.argv) != 3: # 인자 값이 부족할 때
    print("How to use : python3 pyTCPIP_client.py [IP] [PORT]")
    exit() 
IP = str(sys.argv[1]) # 첫번째 인자 값을 IP주소로 받음
PORT = int(sys.argv[2]) # 두번째 인자 값을 PORT번호로 받음
sock.bind((IP, PORT)) # IP와 PORT 바인딩
sock.listen(10) # 최대 10개까지 리스닝
  
c_list = [] 
  
def c_thread(conn, addr): 
    conn.send(" -- Welcome to chatroom! -- ") # 정상 접속 시 클라이언트에 메세지 송출
  
    while True: 
            try: # 수신받은 메세지를 출력
                msg = conn.recv(4096) 
                if msg: 
                    send_msg = "[ " + addr[0] + " ] " + msg
                    broadcast(send_msg, conn)
                    # 다중 접속 채팅방을 구현하기 위해 모든 클라이언트에게 메세지를 보냄
                    print("[ " + addr[0] + " ] " + msg)
                else: 
                    remove(conn) 
            except: 
                continue
  
def broadcast(msg, conn) : # line 28
    for c in c_list : 
        if c != conn : 
            try: 
                c.send(msg) 
            except: 
                c.close() 
                remove(c) 
  
def remove(conn): # 연결 해제 함수
    if conn in c_list: 
        c_list.remove(conn) 
  
while True: 
    conn, addr = sock.accept() # 연결 요청 시 수락하고,
    c_list.append(conn) # 새로 연결된 클라이언트를 클라이언트 목록에 저장
    print(" -- " + addr[0] + " entered chatroom! -- ")
  
    start_new_thread(c_thread,(conn,addr)) # 각 사용자들의 쓰레드 생성
  
conn.close() 
server.close() 
