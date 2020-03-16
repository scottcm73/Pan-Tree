from flask import Flask, request, render_template, redirect
from flask_bootstrap import flask_bootstrap
from flask_wtf import Flaskform
from wtf
import datetime

app = Flask(__name__)

#place in a different file
app.secret_key = 'myprecious'
class LoginForm(Flaskform):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(Flaskform):
    email = StringField('email', validator=[InputRequired90, Email(message="Invalid Email"), Length=(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')

@app.route('/index.html')

@app.route('/home.html')

@app.route('/signup.html')

@app.route('/dashboard.html')

app.run(debug=True)