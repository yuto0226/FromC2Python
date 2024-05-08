import socket
target_addr = ("127.0.0.1", 8080)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

if not s:
    print("fail to create socket.")

s.settimeout(100)

s.connect(target_addr)

while True:
    request = input(f"to {target_addr[0]}:{target_addr[1]} < ")

    if request == "":
        request = "NONE\r\n"
    elif request == "quit":
        s.send(bytes(b"QUIT\r\n"))
        s.close()
        break

    s.send(bytes(request, "utf-8"))
    while not s.recv(2048) == bytes(request, "utf-8"):
        print("Try to resend data.")
        s.send(encode(request))

s.close()
