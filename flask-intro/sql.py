import sqlite3

with sqlite3.connect('sample.db') as connection:
	c=connection.cursor()
	c.execute("""CREATE TABLE posts(tilte TEXT, description TEXT)""")
	c.execute('INSERT INTO posts VALUES Hell yeah", "I\'m fine")')
	c.execute('INSERT INTO posts VALUES "Testing data", "I\'m testing data")')