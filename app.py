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
from sqlalchemy import create_engine, func
from werkzeug.security import generate_password_hash, check_password_hash
from app_config import USER, PASSWORD, HOST, PORT, DATABASE, DIALECT, DRIVER, secret
#from testconfig import DIALECT, DRIVER, USERNAME, PASSWORD, DATABASE, HOSTNAME, PORT

db_uri = f"{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}/{DATABASE}"


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

#@login_required
# Temporarily taken out because I want to get to page without having to login.
# I still have to type in /dashboard to ensure I get to the page.
def dashboard():
    engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}") 


    with engine.begin() as connection:
        rs = connection.execute ('Select * from order_products_prior opp\
            LEFT JOIN orders o ON opp.order_id = o.order_id\
            LEFT JOIN products p ON p.product_id = opp.product_id\
            LEFT JOIN departments d ON d.department_id = p.department_id\
            WHERE o.user_id=5;')
        
        x=0
        #Ensures that it is a valid json with single root.
        data="{\"product_order\":["
        for row in rs:
            data=data+str(dict(row))+","
            x=x+1 # counts the rows returned
        data=data.replace("'", "\"")
        data = data[:-1] # Erases final comma
        data = data + "]}"

    connection.close()
    return render_template("dashboard.html", data=data)
# need to pass name=current_user.username

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True, port=5001)

