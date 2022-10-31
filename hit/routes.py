from flask import Flask
from hit.utils.hitcount import get_hit_count

app = Flask(__name__)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"



