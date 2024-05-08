import socket
target_addr = ("127.0.0.1", 8080)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

if not s:
    print("fail to create socket.")

s.settimeout(100)

"""
與 server 溝通
"""
def communicate():
    while True:
        request = input(f"to {target_addr[0]}:{target_addr[1]} < ")

        """
        設定特殊資料
        """
        if request == "":
            request = "NONE\r\n"
        elif request == "quit":
            s.send(bytes(b"QUIT\r\n"))
            s.close()
            break

        """
        傳送資料
        """
        try:
            s.send(bytes(request, "utf-8"))
        except ConnectionResetError:
            print("Server is down.")
            s.close()
            break


try:
    s.connect(target_addr)
    communicate()
except ConnectionRefusedError:
    print("Connection is refused.")
