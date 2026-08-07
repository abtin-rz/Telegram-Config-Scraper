# export http_proxy=http://127.0.0.1:10809                                                                               ✔ 
# export https_proxy=http://127.0.0.1:10809
# export HTTP_PROXY=http://127.0.0.1:10809
# export HTTPS_PROXY=http://127.0.0.1:10809

import requests
from bs4 import BeautifulSoup

# ===================== تنظیمات =====================

URL_CODE = "https://t.me/s/filembad"
URL_BR = ""
# https://t.me/s/farah_vpn

OUTPUT_FILE = "soup.txt"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "Chrome/138.0 Safari/537.36"
    )
}

ALLOWED_PREFIXES = (
    "vless://",
    "vmess://",
    "ss://",
    "trojan://",
)

# مجموعه برای حذف موارد تکراری
configs = set()

# ===================== توابع =====================

def get_soup(url):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")


def add_configs(items):

    for item in items:

        text = item.strip()

        if not text:
            continue

        if not text.startswith(ALLOWED_PREFIXES):
            continue

        configs.add(text)


def extract_code(url):

    soup = get_soup(url)

    return [
        code.get_text(strip=True)
        for code in soup.find_all("code")
    ]


def extract_br(url):

    soup = get_soup(url)

    result = []

    for message in soup.select(".tgme_widget_message_text"):

        text = message.get_text(
            separator="\n",
            strip=True
        )

        if not text:
            continue

        result.extend(text.splitlines())

    return result


# ===================== اجرا =====================

add_configs(extract_code(URL_CODE))
add_configs(extract_br(URL_BR))

# نوشتن فایل از ابتدا
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

    for config in sorted(configs):
        file.write(config)
        file.write("\n\n")
