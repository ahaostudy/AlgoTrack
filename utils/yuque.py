import re
import requests
from config import config
from utils.image import load


def get_books(book_id: int, pattern: str, sort: bool) -> list:
    url = f'https://www.yuque.com/api/docs?book_id={book_id}'
    data = requests.get(url).json().get('data')
    books = []
    for i in data:
        if not pattern or re.match(pattern, i.get('title')):
            books.append({'id': i.get('id'), 'title': i.get('title')})
    if sort: books.sort(key=lambda x: x.get('title'))
    return books


def get_comments() -> list:
    comments = list()
    url = lambda id: f"https://www.yuque.com/api/comments/floor?commentable_id={b.get('id')}&commentable_type=Doc"
    books = get_books(config.BOOK_ID, config.PATTERN, True)
    for b in books:
        comment = dict()
        title = b.get('title').encode().decode()
        comment['title'] = title
        comment['comments'] = list()
        res = requests.get(url(id))
        bc = res.json().get('data').get('comments')
        for c in bc:
            user = c.get('user').copy()
            user['avatar_url'] = load(user.get('avatar_url'))
            comment['comments'].append(user)
        comments.append(comment)
    return comments
