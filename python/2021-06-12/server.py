import socket
import argparse
import threading
import datetime
host = "127.0.0.1"
port = 4000
user_list = {}
notice_flag = 0
def message(msg):
    print(msg)
    for con in user_list.values():
        try:
            con.send(msg.encode('utf-8'))
        except:
            print("연결이 비 정상적으로 종료된 소켓 발견")
def receive(client_socket, addr, user):

    msg = f"{datetime.datetime.now()} :[  {user}님이 들어오셨습니다.  ]"
    message(msg)
    while 1:
        data = client_socket.recv(1024)
        string = data.decode('utf-8')
        if "/종료" in string:
            msg = f"{datetime.datetime.now()} :[Notice- {user}님이 나가셨습니다.   ]"
            # 유저 목록에서 방금 종료한 유저의 정보를 삭제
            del user_list[user]
            message(msg)
            break
        string = f"( {datetime.datetime.now()} ) [  {user}  ]: {string}"
        message(string)
    client_socket.close()

def notice(client_socket, addr, user):
    pass
def accept(): #IPv4 체계, TCP 타입 소켓 객체를 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(10)
    while 1:
        try:
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            for user, con in user_list:
                con.close()
            server_socket.close()
            break
        user = client_socket.recv(1024).decode('utf-8')
        user_list[user] = client_socket
        #accept()함수로 입력만 받아주고 이후 알고리즘은 핸들러에게 맡긴다.
        notice_thread = threading.Thread(target=notice, args=(client_socket, addr, user))
        notice_thread.daemon = True
        notice_thread.start()
        receive_thread = threading.Thread(target=receive, args=(client_socket, addr,user))
        receive_thread.daemon = True
        receive_thread.start()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="\nJoo's server\n-p port\n")
    parser.add_argument('-p', help="port")
    args = parser.parse_args()
    try:
        port = int(args.p)
    except:
        pass
    accept()

