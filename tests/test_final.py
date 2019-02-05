import json
import unittest

from app import create_app
"""importing the flask app contnained in the __init__ file from the app directory"""


class TestMyBlog(unittest.TestCase):
    """class for testing my_blog"""

    def setUp(self):
        """This method is used to construct all our tests"""
        app = create_app('testing')
        app.testing = True
        self.client = app.test_client()
        self.data = {
            "tittle": 'JESUS CHRIST',
            "description": 'Jesus is the son of living God',

        }
        self.update = {
            "tittle": 'UPDATE: JESUS CHRIST',
            "description": 'UPDATE: Jesus is the son of living God',

        }

        self.incomplete = {
            "tittle": "",
            "description": ""
        }

    def tearDown(self):
        self.data.clear()

    def test_posting_ablog(self):
        resp = self.client.post(path='/api/v1/blog', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json['message'], 'ok')

    def test_getting_all_blogs(self):
        resp = self.client.get(path='/api/v1/blog', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(b'ok' in resp.data)

    def test_getting_asingle_blog(self):
        path = '/api/v1/blog/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_editing_ablog(self):
        path = '/api/v1/blog/1'
        response = self.client.put(path, data=json.dumps(self.update), content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_deleting_ablog(self):
        path = '/api/v1/blog/1'
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_posting_missing_field_and_invalid_input(self):
        resp = self.client.post(path='/api/v1/blog', data=json.dumps(self.incomplete), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(b'Inverid or missing fields' in resp.data)


if __name__ == '__main__':
    unittest.main()
