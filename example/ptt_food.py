from bs4 import BeautifulSoup
import requests
root = "https://www.ptt.cc"
q = "/bbs/Food/index.html"
r = requests.get(root + q)
print("responce:", r)


soup = BeautifulSoup(markup=r.text, features="html.parser")

for i in range(4):
    print("-" * 5 + f"第 {i+1} 頁" + "-" * 5)
    # 抓下一頁的連結
    all_a = soup.select("div.btn-group > a")
    q = all_a[3]["href"]

    titles = soup.find_all("div", class_="title")
    for line in titles:
        print(line.a.get_text())
        print(root + line.a["href"])

        # make a new request
        r = requests.get(root + q)
        soup = BeautifulSoup(markup=r.text, features="html.parser")
