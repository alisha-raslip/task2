import unittest
from app import create_app

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_get_items(self):
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)

    def test_post_item(self):
        response = self.app.post('/items', json={"name": "Test Item", "description": "A test item"})
        self.assertEqual(response.status_code, 201)

    def test_invalid_post(self):
        response = self.app.post('/items', json={"name": 123})
        self.assertEqual(response.status_code, 400)
