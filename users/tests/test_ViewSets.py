from rest_framework.test import APITestCase
from users.models import User


class TestUsersViewSet(APITestCase):
    def setUp(self):
        for ii in range(0, 5):
            User.objects.create(
                first_name=f"Test user first name {ii}",
                last_name=f"Test user last name {ii}",
                address=f"Test user address {ii}",
            )

        self.payload = {
            "first_name": "Angel",
            "last_name": "Ibrahim",
            "address": "test address",
        }

    def test_should_get_user_list(self):
        response = self.client.get("/users/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(5, len(response.json()))

    def test_should_create_user(self):
        self.assertEqual(5, User.objects.count())
        response = self.client.post("/users/", data=self.payload)
        self.assertEqual(201, response.status_code)
        self.assertEqual(6, User.objects.count())
