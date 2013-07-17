from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import hashers
from django.contrib.auth.models import User
from online_store.models import *
from django.core.urlresolvers import reverse

class UserAuthenticationViewTests(TestCase):

  def test_user_signup(self):
    "Posting to signup should create a new user with the right fields"
    test_client = Client()
    test_client.post(reverse('signup'), {'username':'test user',
                                        'email' : 'test@gmail.com',
                                        'password' : 'password',
                                        'confirm_password' :'password'})

    queryset = User.objects.filter(username='test user')
    self.assertEquals(queryset.count(), 1)
    self.assertEquals(queryset[0].username, 'test user')
    self.assertEquals(queryset[0].email, 'test@gmail.com')
    self.assertEquals(hashers.check_password('password',queryset[0].password), True)


  def test_user_login(self): 
    "Posting to login should add user id to session"
    username = 'test user'
    email = 'test@gmail.com'
    password = 'password'
    user = User.objects.create_user(username, email, password)
    test_client = Client()
    test_client.post(reverse('login'),{'username':username, 'password' : password})

    self.assertEquals(test_client.session['_auth_user_id'], user.id)


  def test_user_logout(self): 
    "Visitin logout should clear the user id from the session"
    test_client = Client()
    test_client.session['_auth_user_id'] = 1
    test_client.get(reverse('logout'))
    self.assertNotIn('_auth_user_id', test_client.session)

