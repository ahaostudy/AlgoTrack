from flask_restful import Api
from api import api as a


def init_router(app):
    api = Api(app)
    api.add_resource(a.Comment, '/comment')
    api.add_resource(a.Image, '/image/<string:img>')
