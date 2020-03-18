from flask import Flask, request, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from app_config import username, password, server, database
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
#from wtf
import datetime

app = Flask(__name__)
Bootstrap(app)

db_uri = f"mysql://{username}:{password}@{server}/{database}"
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

db = SQLAlchemy(app)

#place in a different file
app.secret_key = 'myprecious'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid Email")])
    username = StringField('username', validators=[InputRequired(), Length(min=4,  max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
def land():
    return render_template('login.html')

@app.route('/index.html')

@app.route('/login.html')
def login():
    form = LoginForm()

    return render_template('login.html', )

@app.route('/signup.html')
def signup():
    form = RegisterForm()

    return render_template('signup.html', form=form)

@app.route('/dashboard.html')
def some():
    return None

app.run(debug=True)