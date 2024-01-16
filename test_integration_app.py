import unittest
from flask import Flask
from app import app

class TestAppIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_and_delete_item(self):
        # Add item
        response_add = self.app.post('/add', data={'item': 'Integration Test Item'})
        self.assertEqual(response_add.status_code, 302)  # Redirect status code

        # Verify item added
        response_index = self.app.get('/')
        self.assertIn(b'Integration Test Item', response_index.data)

        # Delete item
        response_delete = self.app.get('/delete/0')
        self.assertEqual(response_delete.status_code, 302)  # Redirect status code

        # Verify item deleted
        response_index_after_delete = self.app.get('/')
        self.assertNotIn(b'Integration Test Item', response_index_after_delete.data)

if __name__ == '__main__':
    unittest.main()
