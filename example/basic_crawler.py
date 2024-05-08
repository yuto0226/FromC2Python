import requests
import re

root_url = "https://selquery.ttu.edu.tw/Main/ViewClass.php"

para = {
    "SelDp": "06",      # Department
    "SelCl": "UI2B"     # Class
}

responce = requests.get(url=root_url, params=para)
print("Status Code: ",responce.status_code)
