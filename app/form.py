from app import app
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Regexp

class NameForm(Form):
    name = StringField("enter your name:", validators=[Required()])
    password = PasswordField("your password: (5-8 characters)", validators=[Regexp("(.){5,8}")])
    submit = SubmitField("Submit")

    
