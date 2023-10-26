import pdb
from datetime import datetime

from rest_framework.test import APITestCase
from rest_framework import status

from nubi.utils.enums.sex_type import SexType


class UserCreateAPITestCase(APITestCase):
    """User create API test case"""

    def setUp(self):
        self.valid_email = "email@mail.com"
        self.valid_name = "santiago"
        self.valid_last_name = "feliu"
        self.valid_sex_type = SexType.MALE
        self.valid_dni = "39393939"
        birth_date = datetime.strptime("2023-10-23", "%Y-%m-%d")
        self.valid_birth_date = birth_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    def test_create_user_successfull(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            f"error message {response.json()}",
        )
        for data_key in data.keys():
            self.assertEqual(
                response.json()[data_key],
                data[data_key],
                f"{data_key} de response es distinto"
            )

    def test_create_user_invalid_email_error(self):
        url = "/users/"
        data = {
              "email": "estoesunmailincorrecto",
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

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

    def test_create_user_no_email_error(self):
        url = "/users/"
        data = {
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

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

    def test_create_user_not_unique_email_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)
        data["dni"] = '39393931'
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )
        self.assertIn(
            "email",
            response.json().keys(),
            f"Cuerpo del response es distinto"
        )

    def test_create_user_no_name_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )

        self.assertIn(
            "name",
            response.json(),
            f"Error inesperado {response.json()}"
        )

    def test_create_user_no_last_name_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            f"error message {response.json()}",
        )

        self.assertIn(
            "last_name",
            response.json(),
            f"Error inesperado {response.json()}"
        )

    def test_create_user_invalid_sex_type_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": "Z",
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

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

    def test_create_user_no_sex_type_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

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

    def test_create_user_long_dni_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": "393428885",
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

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

    def test_create_user_not_numeric_dni_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": "noesdni1",
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

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

    def test_create_user_no_dni_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)

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

    def test_create_user_not_unique_dni_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": self.valid_birth_date
        }
        response = self.client.post(url, data)
        data["email"] = "otro@email.com"
        response = self.client.post(url, data)

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

    def test_create_user_invalid_birth_date_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni,
              "birth_date": "noesunafecha"
        }
        response = self.client.post(url, data)

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

    def test_create_user_no_birth_date_error(self):
        url = "/users/"
        data = {
              "email": self.valid_email,
              "name": self.valid_name,
              "last_name": self.valid_last_name,
              "sex_type": self.valid_sex_type,
              "dni": self.valid_dni
        }
        response = self.client.post(url, data)

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