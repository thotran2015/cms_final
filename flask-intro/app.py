# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session,flash, g
from functools import wraps
import sqlite3
# create the application object
app = Flask(__name__)
app.secret_key='hi'
#indicate that database exist
app.database='sample.db'

#login required decorator/ login page is always popped up first
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap



# use decorators to link the function to a url
@app.route('/')
# call the func login_required to make sure people are loggined in to enter home page.
@login_required
def home():
	#create a db connection obj right after logged in
	g.db=connect_db()
	#query the database/fetching data from the database
	cur=g.db.execute('select * from posts')
	#store the fetched data in dictionaries, each post is in form of a dictionary
	posts=[dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	#close database
	g.db.close()
	return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template




@app.route('/login', methods=['GET', 'POST'])
def login():
        error = None
        level = None
        if request.method == 'POST':
                level = request.form['level']
                return redirect(url_for('mood_map'))

        else:
                error = 'no emotions. please try again'
        return render_template('login.html', error=error, level = level)


@app.route('/mood_map')
def mood_map():
    return render_template('vizpage.html')  # render a template

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You are logged out')
	return redirect(url_for('welcome'))

#connect the app to the database
def connect_db():
	return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
