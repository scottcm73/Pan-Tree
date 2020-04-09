from flask import (
    Flask,
    request,
    render_template,
    render_template_string,
    redirect,
    url_for,
    jsonify,
    _app_ctx_stack,
)
from flask_bootstrap import Bootstrap
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from flask_cors import CORS
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, func, update
from sqlalchemy.orm import scoped_session
from werkzeug.security import generate_password_hash, check_password_hash
from app_config import secret, USER, PASSWORD, HOST, PORT, DATABASE, DIALECT, DRIVER
from database import SessionLocal, engine, Base, SQALCHEMY_DATABASE_URL

from models import (
    DictMixIn,
    RegisterForm,
    LoginForm,
    Products,
    Departments,
    Aisles,
    T_Orders,
    T_Order_products
)
import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='/static')
    db.init_app(app)
    return app


app = create_app()

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = SQALCHEMY_DATABASE_URL
app.config['JSON_SORT_KEYS'] = False

app.secret_key = secret
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

##addtitions to use simple SQLAlchemy
CORS(app)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

class User(Base, UserMixin, DictMixIn, db.Model,):
    extend_existing=True
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(15), unique=True)
    email = Column(String(50), unique=True)
    passw = Column(String(80))

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/")
def home_page():
    return redirect('/login')


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
            username=form.username.data, email=form.email.data, passw=hashed_password,
        )
        db.create_all()
        db.session.add(new_user)
        db.session.commit()
        return "<h2>New user has been created, please <a href='/login'>log in</a>.</h2>"

    return render_template("register.html", form=form)


@app.route("/dashboard")
@login_required
def dashboard():

    return render_template("dashboard.html", name=current_user.username)

@app.route("/dashboard-data",)
def dashboard_data():
    query = app.session.query(
        T_Orders.user_id,
        T_Orders.order_date,
        T_Order_products.order_id,
        Products.product_name,
        T_Order_products.quantity,
        Products.price,
        Departments.department,
        Aisles.aisle
        ).join(
            T_Orders, T_Order_products.order_id == T_Orders.order_id
        ).join(
            Products, T_Order_products.product_id == Products.product_id, isouter=True
        ).join(
            Departments, Products.department_id == Departments.department_id
        ).join(
            Aisles, Products.aisle_id == Aisles.aisle_id
        ).filter(
            T_Orders.user_id==5
        )
    qqq = [q._asdict() for q in query]

    return jsonify(qqq)

#this route will be modified to fit the current user
@app.route('/table_data',  methods=['GET'])
def table_data():
    query = app.session.query(
        T_Orders.user_id,
        T_Order_products.order_id,
        T_Orders.order_date.label('Date'),
        Products.product_name.label('Product'),
        T_Order_products.product_id,
        T_Order_products.quantity.label('Amount Bought'),
        T_Order_products.q_left.label('Amount Left'),
        T_Order_products.trash
    ).join(
        T_Order_products, T_Orders.order_id == T_Order_products.order_id
    ).join(
        Products, T_Order_products.product_id == Products.product_id
    ).filter(
        T_Order_products.trash == 0
    ).filter(
        T_Order_products.q_left != 0
    ).all()

    query_dict = [qu._asdict() for qu in query]

    return jsonify(query_dict)

@app.route('/inventory_table')
@login_required
def table():
    return render_template('tables.html')

@app.route('/budget_plot')
@login_required
def budget_plot():
    return render_template('charts.html')

@app.route('/cook_buttons/<order_id>/<product_id>', methods=['GET', 'POST'])
def cook_button(order_id, product_id):
    product = app.session.query(
        T_Order_products
    ).filter(
        T_Order_products.order_id == order_id
    ).filter(
        T_Order_products.product_id == product_id
    ).update({ 'q_left' : (T_Order_products.q_left - 1) })

    app.session.flush()
    app.session.commit()

    return redirect('/inventory_table')

@app.route('/trash_buttons/<order_id>/<product_id>', methods=['GET', 'POST'])
def trash_button(order_id, product_id):
    product = app.session.query(
        T_Order_products
    ).filter(
        T_Order_products.order_id == order_id
    ).filter(
        T_Order_products.product_id == product_id
    ).update({ 'trash' : 1})

    app.session.flush()
    app.session.commit()

    return redirect('/inventory_table')

###routes the data properly joined
##displays correct data
@app.route("/data")
def data():
    query = app.session.query(
        Orders.user_id,
        Orders.order_date,
        Order_products.order_id,
        Products.product_name,
        Order_products.quantity,
        Products.price,
        Departments.department,
        Aisles.aisle
        ).join(
            Order_products, Orders.order_id == Order_products.order_id
        ).join(
            Products, Order_products.product_id == Products.product_id
        ).join(
            Departments, Products.department_id == Departments.department_id
        ).join(
            Aisles, Products.aisle_id == Aisles.aisle_id
        ).limit(100).all()
    
    qqq = [q._asdict() for q in query]

    return jsonify(qqq)


@app.route("/data/<order_id>")
def data_for_order(order_id):
    query = app.session.query(
        Orders.user_id,
        Orders.order_date,
        Order_products.order_id,
        Products.product_name,
        Products.price,
        Departments.department,
        Aisles.aisle
        ).join(
            Order_products, Orders.order_id == Order_products.order_id
        ).join(
            Products, Order_products.product_id == Products.product_id
        ).join(
            Departments, Products.department_id == Departments.department_id
        ).join(
            Aisles, Products.aisle_id == Aisles.aisle_id
        ).filter(
                Order_products.order_id == order_id
        ).all()

    qqq = [q._asdict() for q in query]

    return jsonify(qqq)

@app.route("/product_data")
def product_data():
    query = app.session.query(
        Products.pro
        ).all()

    qqq = [q.to_dict() for q in query]

    return jsonify(qqq)


@app.route("/department_data")
def department_data():
    query = app.session.query(Departments).all()

    qqq = [q.to_dict() for q in query]

    return jsonify(qqq)


@app.route("/aisles_data")
def aisles_data():
    query = app.session.query(Aisles).all()
    qqq = [q.to_dict() for q in query]

    return jsonify(qqq)



@app.route("/plot1")
@login_required
def plot1():

    return render_template("plot1.html", name=current_user.username)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()


if __name__ == "__main__":
    app.run(debug=True, port=5001)
