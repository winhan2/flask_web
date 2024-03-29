# coding: utf-8
import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)