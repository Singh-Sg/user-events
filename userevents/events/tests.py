from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class EventTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='top_secret')
        self.client = Client()

    def test_get_all_event_without_login(self):
        """Test without loging"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_get_all_event_with_login(self):
        """Get all events after login"""
        self.client.login(email='test@test.com', password='top_secret')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_my_events(self):
        """Get my events"""
        self.client.login(email='test@test.com', password='top_secret')
        response = self.client.get('/my-event')
        self.assertEqual(response.status_code, 200)

    def test_create_event(self):
        """Create New events"""
        self.client.login(email='test@test.com', password='top_secret')
        url = '/event/new/'
        response = self.client.post(url, {'title': 'new idea', "description": "8f8e1"})
        self.assertEqual(response.status_code, 201)

    def test_join_event(self):
        """Join Events"""
        self.client.login(email='test@test.com', password='top_secret')
        url = '/event/new/'
        response = self.client.post(url, {'title': 'new idea', "description": "8f8e1"})
        join_url = '/event/join/1'
        response = self.client.get(join_url)
        self.assertEqual(response.status_code, 200)
