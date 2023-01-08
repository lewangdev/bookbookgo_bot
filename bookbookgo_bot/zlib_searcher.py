import requests

from config import ZLIB_SEARCHER_BASE_URL

def search_books(keyword, limit=100):
    url = f"{ZLIB_SEARCHER_BASE_URL}/search"
    query=None
    if type(keyword) is dict:
        query = " ".join(map(lambda f: f'{f[0]}:{f[1]}', filter(lambda f: False if not f[1] else True, keyword.items())))
    elif type(keyword) is str:
        query = keyword
    else:
        return dict(books=[])

    params = dict(query=query, limit=limit)
    r = requests.get(url, params)
    return r.json()

def sort_books(books):
    extensions = ['epub', 'mobi', 'azw3', 'pdf', 'txt']
    books_group_by_ext = {}
    for ext in extensions:
        books_group_by_ext[ext] = []

    for book in books:
        book_ext = book['extension']
        if book_ext not in extensions:
            continue

        books_group_by_ext[book_ext].append(book)

    books_sorted = []
    for ext in extensions:
        books_sorted.extend(books_group_by_ext[ext])

    return books_sorted

if __name__ == "__main__":
    res = search_books('余华')
    print(res)

    res = search_books(dict(title='红楼梦', author='曹雪芹'))
    print(res)
