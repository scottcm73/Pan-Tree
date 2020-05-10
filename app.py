from flask import (
    request,
    render_template,
    render_template_string,
    redirect,
    url_for,
    jsonify
)
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user
)
from models import (
    RegisterForm,
    LoginForm,
    User,
    Products,
    Departments,
    Aisles,
    T_Orders,
    T_Order_products,
    Product_nutrients
)
from queries import (
    department_query, 
    nutrient_query, 
    budgetplot_query,
    count_nutrients
)
from sqlalchemy import create_engine, func, update
from werkzeug.security import generate_password_hash, check_password_hash

from config import app, login_manager, db

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

# signup not available yet.

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

@app.route('/inventory_table')
@login_required
def table():
    return render_template('tables.html')

@app.route("/budget_analysis")
@login_required
def budget_analysis():

    return render_template("budget_analysis.html", name=current_user.username)

@app.route("/nutrient_plot")
def nutrient_plot():
    return render_template("nutrient_plot.html", name=current_user.username)

@app.route("/test_james")
def test_james():
    return render_template("test_james.html", name=current_user.username)

@app.route("/checkout")
def checkout_page():
    return render_template("checkout.html", name=current_user.username)

@app.route("/cart")
def cart_page():
    return render_template("cart.html", name=current_user.username)

@app.route("/budget_data")
@login_required
def budget_data():
    qqq = [q._asdict() for q in budgetplot_query]

    return jsonify(qqq)

#this route will be modified to fit the current user
@app.route('/table_data',  methods=['GET'])
def table_data():
    table_query = app.session.query(
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

    query_dict = [qu._asdict() for qu in table_query]

    return jsonify(query_dict)

@app.route('/cook_buttons/<order_id>/<product_id>', methods=['GET', 'POST'])
def cook_button(order_id, product_id):
    app.session.query(
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
    app.session.query(
        T_Order_products
    ).filter(
        T_Order_products.order_id == order_id
    ).filter(
        T_Order_products.product_id == product_id
    ).update({ 'trash' : 1})

    app.session.flush()
    app.session.commit()

    return redirect('/inventory_table')
    
@app.route("/nutrient_per_order")
def nutrient_per_order():

    query_dicts = [q._asdict() for q in nutrient_query]
    data = count_nutrients(query_dicts)

    return  jsonify(data)


@app.route("/department_data")
def department_data():
    qqq = [q.to_dict() for q in department_query]
    return jsonify(qqq)


@app.route("/aisles_data")
def aisles_data():
    query = app.session.query(Aisles).all()
    qqq = [q.to_dict() for q in query]

    return jsonify(qqq)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
