import socket
import argparse
import threading
import datetime
def handle_receive(lient_socket, user):
    while 1:
        try:
            data = client_socket.recv(1024)
        except Exception as ex :
            print("연결 끊김", ex)
            break
        data = data.decode('utf-8')
        if not user in data:
            print(data)
def handle_send(client_socket):
    while 1:
        data = input(f"{datetime.datetime.now()} :[ 나 ]:")
        client_socket.send(data.encode('utf-8'))
        if data == "/종료":
            break
    client_socket.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="\nclient\n-p port\n-i host\n-s string")
    # 포트를 받는다
    parser.add_argument('-p', help="port")
    # 아이피를 받겠다
    # required=True 이거 없으면 실행 못한다.
    parser.add_argument('-i', help="host", required=True)
    # user을 받는다
    parser.add_argument('-u', help="user", required=True)
    args = parser.parse_args()
    host = args.i
    user = str(args.u)
    try:
        port = int(args.p)
    except:
        pass
        #IPv4 체계, TCP 타입 소켓 객체를 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 지정한 host와 prot를 통해 서버에 접속합니다.
    client_socket.connect((host, port))
    client_socket.send(user.encode('utf-8'))
    receive_thread = threading.Thread(target=handle_receive, args=(client_socket, user))
    receive_thread.daemon = True
    receive_thread.start()
    send_thread = threading.Thread(target=handle_send, args=(client_socket,))
    send_thread.daemon = True
    send_thread.start()
    send_thread.join()
    receive_thread.join()

