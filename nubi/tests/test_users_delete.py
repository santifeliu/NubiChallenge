import pdb

from rest_framework.test import APITestCase
from rest_framework import status

from nubi.models import User


class UserDeleteAPITestCase(APITestCase):
    """User Delete API test case"""

    fixtures = ["nubi/tests/test_users.json"]

    def test_delete_user_successfull(self):
        user = User.objects.first()
        amount_user_before = User.objects.count()
        url = f"/users/{user.pk}/"
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            f"error message {response}",
        )
        amount_user_after = User.objects.count()
        self.assertEqual(amount_user_before - 1, amount_user_after, "Diferencia entre cantidad de usuarios antes y despues de borrado")
        self.assertFalse(User.objects.filter(pk=user.pk).exists(), "Usuario borrado encontrado en DB")