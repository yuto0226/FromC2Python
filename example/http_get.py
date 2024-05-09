import socket

url = "i4010.isrcttu.net"
port = 9996

request_url = 'GET / HTTP/1.1\r\nHost: i4010.isrcttu.net:9996\r\n\r\n'
target_addr = (url, port)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect(target_addr)
s.settimeout(2)

print("--- http request ---")
print(request_url, end="")
print("--------------------")

s.send(request_url.encode())

print(f"--- responce from {url} ---")
rec = s.recv(1024)



response = b""
while rec:
    response += rec
    try:
        rec = s.recv(1024)
    except TimeoutError:
        print("連線超時")
        break
print(response.decode(), end="")
print("-------------------------" + "-" * len(url))
