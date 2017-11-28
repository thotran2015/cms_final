import sqlite3
conn = sqlite3.connect('database.db')
print ("Opened database successfully")

#energetic int, angry int, stressed int, tired int, upset int, sad int, calm int, content int, confused int
conn.execute('CREATE TABLE submissions (happy INTEGER, excited INTEGER, energetic INTEGER, angry INTEGER, stressed INTEGER, confused INTEGER, sad INTEGER, calm INTEGER, tags TEXT)')
             #midterms_exams TEXT, coursework TEXT, job TEXT, friends TEXT, family TEXT, relationship TEXT, extracurriculars TEXT, future TEXT, weather TEXT, politics TEXT, finances TEXT, physical_health TEXT, mental_health TEXT, homesickness TEXT, religious_spiritual TEXT)')

##conn.execute('CREATE TABLE submissions (happy INTEGER, excited INTEGER, energetic INTEGER, angry INTEGER, stressed INTEGER, frustrated INTEGER, upset INTEGER, tired INTEGER, lost INTEGER, sad INTEGER, calm INTEGER, content INTEGER, midterms_exams TEXT, coursework TEXT, job TEXT, friends TEXT, family TEXT, relationship TEXT,extracurriculars TEXT, future TEXT, weather TEXT, politics TEXT, finances TEXT, physical_health TEXT, mental_health TEXT, homesickness TEXT, religious_spiritual TEXT)')
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
