<<<<<<< HEAD
from flask import Flask, request, render_template, redirect, session, flash
import datetime

app = Flask(__name__)

#place in a different file
app.secret_key = 'myprecious'

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }


@app.route('/')
def landing():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'we have an error'
            
        else:
            session['logged_in'] = True 
            flash('You were just logged in!')
            return redirect('/')
    return render_template('home.html', error = error)

@app.route('/logout')
def logout():
    flash('You were just logged out!')
    session.pop('logged_in', None)
    return redirect('/login')


app.run(debug=True)
=======
from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from app_config import secret, DIALECT, DRIVER, username, host, database, password
#from testconfig import DIALECT, DRIVER, USERNAME, PASSWORD, DATABASE, HOSTNAME, PORT

db_uri = f"{DIALECT}+{DRIVER}://{username}:{password}@{host}/{database}"


app = Flask(__name__)

app.secret_key = secret
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"




class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    passw = db.Column(db.String(80))


class LoginForm(FlaskForm):
    username = StringField(
        "username", validators=[InputRequired(), Length(min=4, max=15)]
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )
    remember = BooleanField("remember me")


class RegisterForm(FlaskForm):
    email = StringField(
        "email", validators=[InputRequired(), Email(message="Invalid Email")]
    )
    username = StringField(
        "username", validators=[InputRequired(), Length(min=4, max=15)]
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home_page():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.passw, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect("/dashboard")
            return "<h1> Invalid username or password. </h1>"

    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            passw=hashed_password,
        )
        db.create_all()
        db.session.add(new_user)
        db.session.commit()
        return "<h2>New user has been created, please <a href='/login'>log in</a>.</h2>"

    return render_template("signup.html", form=form)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", name=current_user.username)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


app.run(debug=True)
>>>>>>> a99cf7294c0c9f4a6efe885ed06944dbce5ff2c0
