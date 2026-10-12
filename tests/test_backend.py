import unittest
from backend.app import app


class FreelanceHubBackendTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page_returns_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"FreelanceHub Backend", response.data)

    def test_home_page_contains_running_message(self):
        response = self.client.get("/")
        self.assertIn(
            b"Backend server is running successfully.",
            response.data
        )


if __name__ == "__main__":
    unittest.main()
