import requests
url = "http://i4010.isrcttu.net"
r = requests.get(url)

print(r)
for i in r.headers.items():
    print(i[0] + ":", i[1])
print("\n"+r.text)