from flask import send_file, render_template
from flask_restful import Resource

from utils import yuque


class Comment(Resource):
    def get(self):
        comments = yuque.get_comments()
        return {'code': 200, 'data': comments}


class Image(Resource):
    def get(self, img):
        return send_file(f'image/{img}', mimetype='image/jpeg')
