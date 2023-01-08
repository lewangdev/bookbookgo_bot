#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position

import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from config import BOT_TOKEN, IPFS_GATEWAY_BASE_URL, LOG_LEVEL
from zlib_searcher import search_books, sort_books

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=LOG_LEVEL
)
logger = logging.getLogger(__name__)

TITLE, AUTHOR = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Please input the title of the book\n"
        "Send /cancel to stop this session.\n\n"
    )

    return TITLE


async def title(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s's input: %s", user.first_name, update.message.text)
    title = update.message.text
    r = search_books(title)
    books = r['books']
    books_sorted = sort_books(books)
    context.user_data['books'] = books_sorted
    context.user_data['title'] = title

    if len(books_sorted) == 0:
        text = f'No book found with title: {title}, try another title below.'
        await update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        return TITLE
    else:
        book = books_sorted[0]
        title = book['title']
        author = book['author']
        extension = book['extension']
        ipfs_cid = book['ipfs_cid']
        url_prefix = f"{IPFS_GATEWAY_BASE_URL}/ipfs/"
        url = f"{url_prefix}{ipfs_cid}?filename={title}.{extension}"
        text = f"Title: {title} Author: {author} Extension: {extension} URL: <a href=\"{url}\">Download</a>\n\n" \
        "If the book above isn't your want, specify the author's name below\n" \
        "Send /cancel to stop this session." 

        await update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        return AUTHOR

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    author = update.message.text
    books_saved = context.user_data['books']
    title = context.user_data['title']
    books = list(filter(lambda n: True if author in n['author'] else False, books_saved))
    if len(books) == 0:
        text = f'No book found with title: {title} and author: {author}.'
    else:
        book = books[0]
        title = book['title']
        author = book['author']
        extension = book['extension']
        ipfs_cid = book['ipfs_cid']
        url_prefix = f"{IPFS_GATEWAY_BASE_URL}/ipfs/"
        url = f"{url_prefix}{ipfs_cid}?filename={title}.{extension}"
        text = f"Title: {title} Author: {author} Extension: {extension} URL: <a href=\"{url}\">Download</a>\n\n" \
        "If the book above isn't your want, specify the author's name below\n" \
        "Send /cancel to stop this session." 

    await update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    return AUTHOR


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! Or /start another search", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, title)],
            AUTHOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, author)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
