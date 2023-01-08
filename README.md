# BookBookGo Bot

A telegram bot for searching/downloading z-library books

Visit :  [![telegram-bot](https://img.shields.io/badge/bot-@BookBookGo-blue?logo=telegram)](https://t.me/bookbookgo_bot)

## How to run

0. Get the source code

```sh
git clone https://github.com/lewangdev/bookbookgo_bot.git
```

1. Install dependencies.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

2. Create a file `.env` which contains this.

```text
# Put your actual bot token
# Keep this file secret
# Use https://t.me/botfather to create your bot
BOT_TOKEN =

# https://github.com/book-searcher-org/book-searcher
ZLIB_SEARCHER_BASE_URL = http://127.0.0.1:7070

# https://ipfs.github.io/public-gateway-checker/
IPFS_GATEWAY_BASE_URL = https://ipfs.io

LOG_LEVEL = debug
```

3. Now run `python bootbookgo_bot/main.py`, you may press <kbd>CTRL</kbd> + <kbd>c</kbd> to stop the bot.


More info about [persistence](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Making-your-bot-persistent).

For furthur assistance :  [![telegram-chat](https://img.shields.io/badge/chat-@lewang-blue?logo=telegram)](https://t.me/lewang)




