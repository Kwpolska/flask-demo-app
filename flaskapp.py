# A simple Flask demo app that demonstrates one basic route, favicons,
# and static files. Written for my tutorial,
# Deploying Python Web Applications with nginx and uWSGI Emperor.
# <https://go.chriswarrick.com/pyweb>
# Licensed under the WTFPL.

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return ('<!DOCTYPE html>\n'
            '<meta charset="utf-8">\n'
            '<title>Hello from Flask!</title>\n'
            '<h1>Hello from Flask!</h1><img src="/static/hello.png">\n')
