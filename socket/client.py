import socket

# 접속 정보 설정
# 접속할 서버의 아이피
SERVER_IP = '127.0.0.2'
# 접속할 서버의 포트
SERVER_PORT = 5050
# ?
SIZE = 1024

SERVER_ADDR = (SERVER_IP, SERVER_PORT)

# 클라이언트 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # 위에 입력한 값으로 서버에 접속
    client_socket.connect(SERVER_ADDR)
    # 서버에 메시지 전송
    client_socket.send('hi'.encode())
    # 서버로부터 응답받은 메시지 반환
    msg = client_socket.recv(SIZE)
    # 서버로부터 응답받은 메시지 출력
    print("resp from server : {}".format(msg))