from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>/')
def show_subpath(subpath):
    return 'Subpath %s' %escape(subpath)

if __name__ == '__main__':
    app.run(debug = True)