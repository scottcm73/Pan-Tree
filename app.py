from flask import Flask, request, render_template, redirect, render_template_string
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
from app_config import username, password, server, database


app = Flask(__name__)
Bootstrap(app)

db_uri = f"mysql+mysqlconnector://{username}:{password}@{server}/{database}"
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri



db = SQLAlchemy(app)

#place in a different file
app.secret_key = 'myprecious'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid Email")])
    username = StringField('username', validators=[InputRequired(), Length(min=4,  max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
def home_page():
    # String-based templates
    return render_template('base.html')
#@app.route('/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user:
            if user.password == form.password.data:
                return redirect('/dashboard')
        

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created</h1>'


    return render_template('signup.html', form=form)

@app.route('/dashboard.html')
def some():
    return None

app.run(debug=True)