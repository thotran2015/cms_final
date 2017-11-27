# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session,flash, g
from functools import wraps
import sqlite3
# create the application object
app = Flask(__name__)
app.secret_key='hi'
#indicate that database exist
app.database='database.db'

#login required decorator/ login page is always popped up first
##def login_required(f):
##	@wraps(f)
##	def wrap(*args, **kwargs):
##		if 'logged_in' in session:
##			return f(*args, **kwargs)
##		else:
##			flash('You need to login first')
##			return redirect(url_for('login'))
##	return wrap
##
##@app.route('/welcome')
##def welcome():
##    return render_template('welcome.html')  # render a template

@app.route('/', methods=['GET', 'POST'])
def input():
        return render_template('input.html')

@app.route('/add_submission', methods = ['GET', 'POST'])
def add_submission():
    #<!--(happy int, excited int, energetic int, angry int, stressed int, tired int, upset int, sad int, calm int, content int, confused int)-->
    if request.method =='POST':
        try:
            data = []
            emos=['happy', 'excited', 'energetic', 'angry', 'stressed', 'frustrated', 'upset', 'tired', 'lost', 'sad', 'calm', 'content']
            in_emos= {}
            for emo in emos:
                in_emos[emo]=request.form[emo]
                data.append(request.form[emo])
            tags = ['midterms_exams', 'coursework', 'job', 'friends', 'family', 'relationship', 'extracurriculars', 'future', 'weather', 'politics', 'finances', 'physical_health', 'mental_health', 'homesickness', 'religious_spiritual']
            in_tags=[]
            for tag in tags:
                if request.form.get(tag) =='on':
                    in_tags.append(tag)
            data.append(', '.join(in_tags))
            with connect_db() as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO submissions (happy, excited, energetic, angry, stressed, frustrated, upset, tired, lost, sad, calm, content, tags) VALUES (?"+", ?"*len(emos)+")", data)
                conn.commit()
                msg='Submission recorded successfully'
        except:
            conn.rollback()
            msg = 'error in insert operation'
        finally:
            return render_template('result.html', msg = msg, tag=data)
            conn.close()

# use decorators to link the function to a url
@app.route('/mood_map')
# call the func login_required to make sure people are loggined in to enter home page.
#@login_required
def query_submissions():
	#create a db connection obj right after user input data
	g.db=connect_db()
	#query the database/fetching data from the database
	cur=g.db.execute('select * from submissions')
	#store the fetched data in dictionaries, each submission is in form of a dictionary
	submissions=[dict(sub_num= i, happy=row[0], excited=row[1], energetic = row[2], angry=row[3], stressed =row[4], frustrated =row[5], upset= row[6], tired=row[7],
                          lost =row[8], sad = row[9], calm =row[10], content=row[11],  tags=row[12].split(',')) for i, row in enumerate(cur.fetchall())]
	#close database
	g.db.close()
	return render_template('vizpage.html', submissions=submissions)

##
##
##@app.route('/mood_map')
##def mood_map():
##    return render_template('vizpage.html')  # render a template

##@app.route('/logout')
##@login_required
##def logout():
##	session.pop('logged_in', None)
##	flash('You are logged out')
##	return redirect(url_for('welcome'))

#connect the app to the database
def connect_db():
	return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
