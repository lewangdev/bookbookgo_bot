# BookBookGo Bot

A telegram bot for [book-searcher](https://github.com/book-searcher-org/book-searcher). Create and search books index, create your private library on Telegram.

## Try 👇️

[![telegram-bot](https://img.shields.io/badge/bot-@BookBookGo-blue?logo=telegram)](https://t.me/bookbookgo_bot)

## How to run

### Docker

```sh
sudo docker compose up -d
```

OR

```sh
sudo docker run -d \
-e BOT_TOKEN=<Your TG BOT TOKEN> \
-e BOOK_SEARCHER_BASE_URL=https://zlib.cydiar.com \
--name bookbookgo_bot \
--restart unless-stopped \
lewangdev/bookbookgo_bot

```

### From Source Code

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
BOOK_SEARCHER_BASE_URL = https://zlib.cydiar.com

# https://ipfs.github.io/public-gateway-checker/
IPFS_GATEWAY_BASE_URL = https://ipfs.io

LOG_LEVEL = debug
```

3. Now run `python bookbookgo_bot/main.py`, you may press <kbd>CTRL</kbd> + <kbd>c</kbd> to stop the bot.


## For furthur assistance Or need help to develop a Telegram Bot
[![telegram-chat](https://img.shields.io/badge/chat-@lewang-blue?logo=telegram)](https://t.me/lewang)

