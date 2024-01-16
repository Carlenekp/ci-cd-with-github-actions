from typing import ItemsView
import unittest
from app import app


class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.items = []

    def test_read_page(self):
        # check if the page is loaded
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

    def test_add_item(self):
        # Test adding an item
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        self.assertIn(b'Test Item', response.data)

    def test_delete_item(self):
        # you can refer to the app by using self.app
        # make a post request with self.app.post(...
        self.items = ['Item', 'Item2']
        response = self.app.post('/delete/0')
        self.assertEqual(response.status_code, 405, "Response should be 405 OK")
        self.assertNotIn(b'Item', response.data)
        
    def test_update_item(self):
        pass

if __name__ == '__main__':
    unittest.main()
