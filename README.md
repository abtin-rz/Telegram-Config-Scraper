# Telegram Config Scraper

A simple Python scraper that collects VPN configs from public Telegram channel (@filembad) and you can use it easily to the **Subscription Link** OR copy them in the **soup.txt file**.

## Features

- Extracts configs from Telegram
- Supports:
  - VLESS
  - VMess
  - Shadowsocks
  - Trojan
- Removes duplicates
- Generates `soup.txt`
- Runs automatically with GitHub Actions

## Usage

```bash
pip install -r requirements.txt
python main.py
```

## Subscription

```
https://raw.githubusercontent.com/abtin-rz/Telegram-Config-Scraper/main/soup.txt
```

## License

MIT
