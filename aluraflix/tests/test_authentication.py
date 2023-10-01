from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import base64


class AuthenticationUserTest(APITestCase):
    def setUp(self):
        self.username = 'jhon'
        self.password = 'jhonpassword'
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.credentials = base64.b64encode(
            f'{self.username}:{self.password}'.encode()).decode()

    def test_get_programas_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Basic {self.credentials}')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_programas_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
