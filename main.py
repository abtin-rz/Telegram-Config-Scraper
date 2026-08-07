# export http_proxy=http://127.0.0.1:10809                                                                               ✔ 
# export https_proxy=http://127.0.0.1:10809
# export HTTP_PROXY=http://127.0.0.1:10809
# export HTTPS_PROXY=http://127.0.0.1:10809


import requests
import bs4

url = "https://t.me/s/filembad"

response = requests.get(url)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")

codes = soup.find_all("code")

with open("soup.txt", "w", encoding="utf-8") as file:
    for code in codes:
        file.write(code.get_text(strip=True))
        file.write("\n\n")