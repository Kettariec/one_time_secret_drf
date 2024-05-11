from rest_framework.test import APITestCase, APIClient
from keep_secrets.models import Secret
from rest_framework import status


class SecretTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.secret = Secret.objects.create(text='test text')

    def test_create_secret(self):
        data = {
            "text": 'test text',
            "days": 3
        }
        response = self.client.post(
            'http://127.0.0.1:8000/keep_secrets/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_error_create(self):
        data = {
            "text": 'test text',
            "days": 8
        }
        response = self.client.post(
            'http://127.0.0.1:8000/keep_secrets/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            response.json(),
            {
                'days': ['Ensure this value is less than or equal to 7.']
            }
        )

    def test_no_secret(self):
        response = self.client.get(
            'http://127.0.0.1:8000/keep_secrets/check/test/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )
        self.assertEqual(
            response.json(),
            {
                'detail': 'No Secret matches the given query.'
            }
        )
