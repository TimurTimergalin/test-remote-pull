from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def print_num():
    return "1"


@app.route('/pull')
def pull():
    os.system("git pull")
    return "OK"


if __name__ == '__main__':
    app.run()
