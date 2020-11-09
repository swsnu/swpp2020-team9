from django.test import TestCase, Client
from django.contrib.auth.models import User
import json

class TestCase(TestCase):
    def setUp(self):
       # User.objects.create_user(username='test_id_1', password='test_password_1')
        User.objects.create_user(username='test_id_1', password='test_password_1', email='test_email_1')

    def test_csrf(self):
        # By default, csrf checks are disabled in test client
        # To test csrf protection we enforce csrf checks here
        client = Client(enforce_csrf_checks=True)
        response = client.post('/api/signup/', json.dumps({'email' : 'eamil', 'username': 'chris', 'password': 'chris'}),content_type='application/json')
        self.assertEqual(response.status_code, 403)  # Request without csrf token returns 403 response

        response = client.get('/api/token/')
        csrftoken = response.cookies['csrftoken'].value  # Get csrf token from cookie

        response = client.post('/api/signup/', json.dumps({'email' : 'eamil', 'username': 'chris', 'password': 'chris'}),content_type='application/json', HTTP_X_CSRFTOKEN=csrftoken)
        self.assertEqual(response.status_code, 201)  # Pass csrf protection

        #not allowed method
        response = client.post('/api/token/', HTTP_X_CSRFTOKEN=csrftoken)
        self.assertEqual(response.status_code, 405)



    def test_signup(self):    
        username = 'test_id'
        password = 'test_password'
        email = 'test_email'

        client = Client(enforce_csrf_checks=True)
        response = client.get('/api/token/')
        csrftoken = response.cookies['csrftoken'].value


        response = client.post('/api/signup/',json.dumps({'email' : email, 'username' : username, 'password' : password}),content_type='application/json', HTTP_X_CSRFTOKEN=csrftoken)

        self.assertEqual(response.status_code, 201)

        #not allowed method
        response = client.get('/api/signup/')
        self.assertEqual(response.status_code, 405)

    def test_signin(self):
        username = 'test_id_1'
        password = 'test_password_1'

        client = Client(enforce_csrf_checks=True)
        response = client.get('/api/token/')
        csrftoken = response.cookies['csrftoken'].value

        response = client.post('/api/signin/', json.dumps({'username' : username, 'password' : password}), content_type='application/json', HTTP_X_CSRFTOKEN=csrftoken)
        self.assertEqual(response.status_code, 204)

        #not allowed method
        response = client.get('/api/signin/')
        self.assertEqual(response.status_code, 405)

    def test_signout(self):
        username = 'test_id_1'
        password = 'test_password_1'

        client = Client(enforce_csrf_checks=True)

        response = client.get('/api/token/')
        csrftoken = response.cookies['csrftoken'].value

        response = client.post('/api/signin/', json.dumps({'username' : username, 'password' : password}), content_type='application/json', HTTP_X_CSRFTOKEN=csrftoken)
        self.assertEqual(response.status_code, 204)

        response = client.get('/api/signout/')
        self.assertEqual(response.status_code, 204)




# Create your tests here.
