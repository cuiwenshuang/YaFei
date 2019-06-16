from flask import Flask, render_template, redirect, request, url_for , send_file

app = Flask(__name__)


common_html_path = 'templates'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
