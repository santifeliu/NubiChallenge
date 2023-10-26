import pdb
from datetime import datetime

from rest_framework.test import APITestCase
from rest_framework import status

from nubi.models import User
from nubi.utils.enums.sex_type import SexType


class UserUpdateAPITestCase(APITestCase):
    """User update API test case"""

    fixtures = ["nubi/tests/test_users.json"]

    def setUp(self):
        self.valid_email = "email@mail.com"
        self.valid_name = "santiago"
        self.valid_last_name = "feliu"
        self.valid_sex_type = SexType.MALE
        self.valid_dni = "39393939"
        birth_date = datetime.strptime("2023-10-23", "%Y-%m-%d")
        self.valid_birth_date = birth_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    def validate_user_json(self, user_json):
        user = User.objects.get(pk=user_json['wallet_id'])
        self.assertEqual(user.email, user_json["email"])
        self.assertEqual(user.name, user_json["name"])
        self.assertEqual(user.last_name, user_json["last_name"])
        self.assertEqual(user.sex_type, user_json["sex_type"])
        self.assertEqual(user.dni, user_json["dni"])
        self.assertEqual(user.birth_date.strftime("%Y-%m-%dT%H:%M:%SZ"), user_json["birth_date"])
        self.assertEqual(user.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"), user_json["created_at"])

    def test_update_email_successful(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "email": self.valid_email
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        self.validate_user_json(response.json())

    def test_update_user_invalid_email_error(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "email": "estoesunmailincorrecto",
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )
        self.assertIn(
            "email",
            response.json(),
            f"Error inesperado: {response.json()}"
        )
        self.assertEqual(user.email, User.objects.get(pk=user.pk).email)

    def test_update_user_not_unique_email_error(self):
        user = User.objects.first()
        other_user = User.objects.last()
        url = f"/users/{user.pk}/"
        data = {
              "email": other_user.email
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )
        self.assertIn(
            "email",
            response.json(),
            f"Cuerpo del response es distinto"
        )

    def test_update_user_name_successful(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "name": self.valid_name
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        self.validate_user_json(response.json())

    def test_update_user_last_name_successful(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "last_name": self.valid_last_name
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        self.validate_user_json(response.json())

    def test_update_user_invalid_sex_type_error(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "sex_type": "Z"
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )

        self.assertIn(
            "sex_type",
            response.json(),
            f"Error inesperado: {response.json()}"
        )

    def test_update_user_sex_type_successful(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "sex_type": self.valid_sex_type
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        self.validate_user_json(response.json())

    def test_update_user_long_dni_error(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "dni": "393428885",
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )
        self.assertIn(
            "dni",
            response.json(),
            f"Error inesperado: {response.json()}"
        )

    def test_update_user_not_numeric_dni_error(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "dni": "noesdni1"
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )
        self.assertIn(
            "dni",
            response.json(),
            f"Error inesperado: {response.json()}"
        )

    def test_update_user_dni_successful(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "dni": self.valid_dni
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        self.validate_user_json(response.json())

    def test_update_user_not_unique_dni_error(self):
        user = User.objects.first()
        other_user = User.objects.last()
        url = f"/users/{user.pk}/"
        data = {
              "dni": other_user.dni
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )
        self.assertIn(
            "dni",
            response.json(),
            f"Cuerpo del response es distinto"
        )

    def test_update_user_invalid_birth_date_error(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "birth_date": "noesunafecha"
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )

        self.assertIn(
            "birth_date",
            response.json(),
            f"Error inesperado: {response.json()}"
        )

    def test_update_user_birth_date_successful(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        data = {
              "birth_date": self.valid_birth_date
        }
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        self.validate_user_json(response.json())