from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.contrib import auth

from store.models import Store, Category


class TestView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='1', slug='camera-drones')
        Category.objects.create(name='1', slug='handheld')
        cls.obj_id = Store.objects.create(product_name='1', slug='1', product_content='', product_characteristics='',
                                          product_price=1).pk

    def test_login(self):
        c = Client()
        response = c.post('/login/', {'username': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 200)

    def test_register_success(self):
        c = Client()
        response = c.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                         'password2': 'test_password'})
        self.assertEqual(response.status_code, 302)

    def test_register_not_success(self):
        c = Client()
        response = c.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                         'password2': 'test_password1'})
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        c = Client()
        response = c.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_support(self):
        c = Client()
        response = c.get('/support/')
        self.assertEqual(response.status_code, 200)

    def test_categories_camera_drones(self):
        c = Client()
        response = c.get('/categories/camera-drones/')
        self.assertEqual(response.status_code, 200)

    def test_categories_handheld(self):
        c = Client()
        response = c.get('/categories/handheld/')
        self.assertEqual(response.status_code, 200)

    def test_learn_more(self):
        c = Client()
        response = c.get('/information/1/')
        self.assertEqual(response.status_code, 200)

    def test_main_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_categories(self):
        self.assertEqual(Category.objects.count(), 2)

    def test_create_store_objects(self):
        self.assertEqual(Store.objects.count(), 1)


class TestAccounts(TestCase):
    def test_create_account(self):
        response = self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                                   'password2': 'test_password'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_create_account_not_similar_passwords(self):
        response = self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                                   'password2': 'test_password1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_create_account_not_all_fields(self):
        response = self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_create_account_not_correct_fields(self):
        response = self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                                   'password3': 'test_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_create_account_user_exists(self):
        self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                        'password2': 'test_password'})
        response = self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                                   'password2': 'test_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)

    def test_create_account_simple_password(self):
        response = self.client.post('/register/', {'username': 'test_user', 'password1': '1234',
                                                   'password2': '1234'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_login_account(self):
        self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                        'password2': 'test_password'})
        user = auth.authenticate(username='test_user', password='test_password')
        self.assertNotEqual(user, None)

    def test_login_account_wrong_password(self):
        self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                        'password2': 'test_password'})
        user = auth.authenticate(username='test_user', password='test_password1')
        self.assertEqual(user, None)

    def test_login_account_wrong_username(self):
        self.client.post('/register/', {'username': 'test_user', 'password1': 'test_password',
                                        'password2': 'test_password'})
        user = auth.authenticate(username='test_user1', password='test_password')
        self.assertEqual(user, None)
