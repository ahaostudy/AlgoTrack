from flask import Flask, render_template

from route.route import init_router
from config import config
from flask_cors import CORS

app = Flask(__name__, template_folder='template')


@app.route('/')
def get():
    return render_template('index.html')


if __name__ == '__main__':
    init_router(app)
    CORS(app)
    config.root_path = app.root_path
    app.run(host=config.HOST, port=config.PORT, debug=True)
