import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SECRET_KEY = "\x05e\xd6\xcd\xb23\xc8\x93Me"

# create my first serious application :)
app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
    app.run(debug=True)
