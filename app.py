from flask import Flask

from flask import request

import os
from flask import Flask, render_template, url_for, json, Response, send_from_directory


app = Flask(__name__, static_url_path='')
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/.well-known/apple-app-site-association')
def return_apple_cert2():
    return get_json_data("apple-app-site-association")

@app.route('/apple-app-site-association')
def return_apple_cert():
    return get_json_data("apple-app-site-association")


def get_json_data(file_name):
    json_url = os.path.join(SITE_ROOT, "static/", file_name)
    data = json.load(open(json_url))
    return Response(json.dumps(data), mimetype='application/json')


if __name__ == '__main__':
    app.run()
