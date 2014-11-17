from app import app
from flask import render_template, request, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from app.form import NameForm

Bootstrap(app) ## use bootstrap to fly :)
Moment(app) ## use moment.js to handle user time

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow(),
                           name=session.get("name"))

@app.route('/login', methods=["GET", "POST"])
def login():
    form=NameForm()
    if request.method == "POST" and form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("your name is successfully changed")
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template("signup.html",
                           form=form)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", error=e), 500
