import socket

# 통신 정보 설정
IP = '127.0.0.2'
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

# 서버 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # 주소 바인딩
    server_socket.bind(ADDR)
    # 클라이언트의 요청을 받을 준비
    server_socket.listen()

    # 무한루프들어가 accept()상태로 대기
    while True:
        # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
        client_socket, client_addr = server_socket.accept()
        # 클라이언트가 보낸 메시지 반환
        msg = client_socket.recv(SIZE)
        # 클라이언트가 보낸 메시지 출력
        print("[{}] message : {}".format(client_addr,msg))
        # 클라이언트에게 응답
        client_socket.sendall("welcome!".encode())
        # 클라이언트 소켓 종료
        client_socket.close()