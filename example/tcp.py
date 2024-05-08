import threading
import socket

addr = ("127.0.0.1", 8080)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

if not s:
    print("fail to create socket.")

s.bind(addr)

print("Waiting for connection ... ")
s.listen(5)

connections = []

def connection(conn, addr):
    print(f"{addr[0]}:{addr[1]} connected.")
    while True:
        receive = conn.recv(2048)

        if receive == b"QUIT\r\n" or receive == b"":
            conn.close()
            print(f"{addr[0]}:{addr[1]} connection closed.")
            return
        print(f"{addr[0]}:{addr[1]} -> {receive.decode()}")
        conn.send(receive)

    conn.close()

def server():
    while True:
        conn, addr = s.accept()  # 接收連線
        new_connection = threading.Thread(target=connection, args=(conn, addr))
        connections.append(new_connection)
        new_connection.start()

server()

s.close()
