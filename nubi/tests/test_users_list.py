import pdb

from rest_framework.test import APITestCase
from rest_framework import status

from nubi.models import User


class UserListAPITestCase(APITestCase):
    """User List API test case"""

    fixtures = ["nubi/tests/test_users.json"]

    def validate_user_json(self, user_json):
        temp_user = User.objects.get(pk=user_json['wallet_id'])
        self.assertEqual(temp_user.email, user_json["email"])
        self.assertEqual(temp_user.name, user_json["name"])
        self.assertEqual(temp_user.last_name, user_json["last_name"])
        self.assertEqual(temp_user.sex_type, user_json["sex_type"])
        self.assertEqual(temp_user.dni, user_json["dni"])
        self.assertEqual(temp_user.birth_date.strftime("%Y-%m-%dT%H:%M:%SZ"), user_json["birth_date"])
        self.assertEqual(temp_user.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"), user_json["created_at"])

    def test_list_user_successfull(self):
        url = "/users/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )
        users = User.objects.all()
        self.assertEqual(len(users), response.json()["count"])
        for user_json in response.json()["results"]:
            self.validate_user_json(user_json)
        while response.json()["next"] is not None:
            response = self.client.get(response.json()["next"])
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK,
                f"error message {response.json()}",
            )
            for user_json in response.json()["results"]:
                self.validate_user_json(user_json)

    def test_match_filter_list_user(self):
        url = "/users/?email=Elva.Bergnaum26@gmail.com"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"error message {response.json()}",
        )

        self.assertEqual(
            response.json()['count'],
            1,
            f"error message {response.json()}",
        )
        self.validate_user_json(response.json()["results"][0])

    def test_order_filter_list_user(self):
        url = "/users/?ordering=email"
        users = list(User.objects.order_by("email").all())
        user_position = 0
        while user_position < 100:
            response = self.client.get(url)
            url = response.json()["next"]
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK,
                f"error message {response.json()}",
            )
            for user_json in response.json()["results"]:
                self.assertEqual(user_json['wallet_id'], str(users[user_position].pk))
                user_position += 1

    def test_inverse_order_filter_list_user(self):
        url = "/users/?ordering=-email"
        users = list(User.objects.order_by("-email").all())
        user_position = 0
        while user_position < 100:
            response = self.client.get(url)
            url = response.json()["next"]
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK,
                f"error message {response.json()}",
            )
            for user_json in response.json()["results"]:
                self.assertEqual(user_json['wallet_id'], str(users[user_position].pk))
                user_position += 1