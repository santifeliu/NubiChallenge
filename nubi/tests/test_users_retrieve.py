import pdb

from rest_framework.test import APITestCase
from rest_framework import status

from nubi.models import User


class UserRetrieveAPITestCase(APITestCase):
    """User Retrieve API test case"""

    fixtures = ["nubi/tests/test_users.json"]

    def test_retrieve_user_successfull(self):
        user = User.objects.first()
        url = f"/users/{user.pk}/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        self.assertEqual(str(user.pk), response.json()["wallet_id"])
        self.assertEqual(user.email, response.json()["email"])
        self.assertEqual(user.name, response.json()["name"])
        self.assertEqual(user.last_name, response.json()["last_name"])
        self.assertEqual(user.sex_type, response.json()["sex_type"])
        self.assertEqual(user.dni, response.json()["dni"])
        self.assertEqual(user.birth_date.strftime("%Y-%m-%dT%H:%M:%SZ"), response.json()["birth_date"])
        self.assertEqual(user.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"), response.json()["created_at"])