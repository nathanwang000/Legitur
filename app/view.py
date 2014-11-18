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
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("your successfully changed your name")
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template("signup.html",
                           form=form,
                           signup=False)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form=NameForm()
    from app.models import User, Role
    from app import db
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data,
                        role_id = 2)
            db.session.add(user)
            session["name"] = form.name.data
            flash("successfully registered, %s" % form.name.data)
        else:
            flash("username %s is taken" % form.name.data, 'error')
    return render_template("signup.html",
                           form=form,
                           signup=True)
    
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", error=e), 500
