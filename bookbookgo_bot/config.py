import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ZLIB_SEARCHER_BASE_URL = os.getenv('ZLIB_SEARCHER_BASE_URL')
IPFS_GATEWAY_BASE_URL = os.getenv('IPFS_GATEWAY_BASE_URL', 'https://ipfs.io')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'info').upper()
