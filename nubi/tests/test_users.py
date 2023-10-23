from rest_framework.test import APITestCase
from rest_framework import status

from nubi.utils.enums.sex_type import SexType


class UserWalletBasicAPITestCase(APITestCase):
    """Wallet API test case"""

    def setUp(self):
        self.valid_email = "email@mail.com"
        self.valid_name = "santiago"
        self.valid_last_name = "feliu"
        self.valid_sex_type = SexType.MALE
        self.valid_dni = "39393939"
        self.valid_birth_date = "2023-10-23"

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
        request = self.client.post(url, data)

        self.assertEqual(
            request.status_code,
            status.HTTP_201_CREATED,
            f"error message {request.json()}",
        )