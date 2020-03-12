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