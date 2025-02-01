import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_moscow_time_response(self):
        """Test if the Moscow time page returns a 200 status code."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_moscow_time_content(self):
        """Test if the response contains the correct HTML structure."""
        response = self.app.get('/')
        self.assertIn(b'Current Moscow Time:', response.data)

if __name__ == "__main__":
    unittest.main()
