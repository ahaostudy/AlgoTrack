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
            books.append({'id': i.get('id'), 'title': i.get('title'), 'slug': i.get('slug')})
    if sort: books.sort(key=lambda x: x.get('title'))
    return books


# 按用户ID去重
def unique(comments: dict):
    if len(comments) == 0: return []
    ans = [comments[0]]
    j = 0
    for i in range(1, len(comments)):
        if comments[i].get('id') != comments[j].get('id'):
            j += 1
            ans.append(comments[i])
    return ans


def get_comments() -> list:
    comments = list()
    url = lambda id: f"https://www.yuque.com/api/comments/floor?commentable_id={b.get('id')}&commentable_type=Doc"
    books = get_books(config.BOOK_ID, config.PATTERN, True)
    for b in books:
        comment = dict()
        comment['title'] = b.get('title')
        comment['slug'] = b.get('slug')
        comment['comments'] = list()
        res = requests.get(url(id))
        bc = res.json().get('data').get('comments')
        for c in bc:
            user = c.get('user').copy()
            user['avatar_url'] = load(user.get('avatar_url'))
            comment['comments'].append(user)
        # 排序去重
        comment['comments'].sort(key=lambda x: x.get('id'))
        comment['comments'] = unique(comment['comments'])
        comments.append(comment)
    return comments
