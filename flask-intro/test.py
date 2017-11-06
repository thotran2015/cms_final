from app import app
import unittest

class TestFlaskCase(unittest.TestCase): 
	#ensure that flask is reponding correctly when requested.
	#we can test the login page bc that is always the first page bc main page always requires login
	#functions' name must start with test
	def test_index(self):
		#create an isolated app that we can send request and test the responses outside of the main app scope
		tester=app.test_client(self)
		#use the unittest library to get the login route and the content in this route
		response=tester.get('/login', content_type='html/text')
		#check the reponse code and ensure that it is =200,  200 means that there was a response after a request
		self.assertEqual(response.status_code,200)


	#ensure that login page loads correctly/ check if right template was rendered since the 1st test might jsut render any template
	def test_login_page_loads(self):
		#create an isolated app that we can send request and test the responses outside of the main app scope
		tester=app.test_client(self)
		#use the unittest library to get the login route and the content in this route
		response=tester.get('/login', content_type='html/text')
		#check the reponse code and ensure that it is =200
		self.assertTrue(b'Please login' in response.data)

	#ensure that log in behaves correctly with right credentials
	def test_correct_login(self):
		#create an isolated app that we can send request and test the responses outside of the main app scope
		tester=app.test_client(self)
		#use the unittest library to get the login route and post something on the page to get a response
		response=tester.post('/login', data=dict(username='admin', password='admin'),follow_redirects=True)
		#check the reponse code and ensure that it is =200
		self.assertIn(b'You are logged in', response.data)


	#ensure that log in behaves correctly with wrong credentials

	def test_incorrect_login(self):
		tester=app.test_client(self)
		response=tester.post('/login', data=dict(username='adminn', password='adminn'),follow_redirects=True)
		self.assertIn(b'Invalid credentials. Please, try again!', response.data)

	#ensure that log-out behaves correctly
	def test_logout(self):
		tester=app.test_client(self)
		tester.post('/login', data=dict(username='admin', password='admin'),follow_redirects=True)
		response=tester.get('/logout', follow_redirects=True)
		self.assertTrue(b'You are logged out' in response.data)

	#ensure that main page requires login
	def test_main_route_requires_login(self):
		tester=app.test_client(self)
		#get the main page route
		response=tester.get('/', follow_redirects=True)
		self.assertTrue(b'You need to login first' in response.data)

	#ensure that logout page requires login
	def test_logout_route_requires_login(self):
		tester=app.test_client(self)
		response=tester.get('/logout', follow_redirects=True)
		self.assertTrue(b'You need to login first' in response.data)

	#ensure that posts show up on main page
	def test_posts_on_main_page(self):
		tester=app.test_client(self)
		response=tester.post('/login', data=dict(username='admin', password='admin'),follow_redirects=True)
		#response=tester.get('/', follow_redirects=True)
		self.assertTrue(b'testing' in response.data)







#need to write test for the enitre app 
#each test should test one functionality 
if __name__=='__main__':
	unittest.main()

