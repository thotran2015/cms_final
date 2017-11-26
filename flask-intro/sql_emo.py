import sqlite3
conn = sqlite3.connect('database.db')
print ("Opened database successfully")

#energetic int, angry int, stressed int, tired int, upset int, sad int, calm int, content int, confused int
conn.execute('CREATE TABLE submissions (happy INTEGER, excited INTEGER, coursework TEXT, exams TEXT, friends TEXT, family TEXT, extracurriculars TEXT, employment TEXT)')
print ("Table created successfully")
conn.close()

##midterms/exams
##coursework
##work/job
##friends
##family
##relationship(s)
##extracurriculars
##weather
##politics
##finances
##physical health
##mental health
##homesickness
##living group/residential life
