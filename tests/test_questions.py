# import json
# from tests.test_base import BaseTestCase


# def test_for_json_data(self):

#    with self.client:
#        response = self.post_blog('MY NEWS', 'I have good news')
#        self.assertTrue(response.content_type, 'application/json')


# def test_json_error_response(self, blog_id):

#    with self.client:
#        response = self.post_blog('MY NEWS', 'I have good news')
#        data = json.loads(response.data.decod())
#        self.asserNotEqual(data.get('message'), 'request should be json')


# def test_ablog_added(self):
#    with self.client:
#        response = self.post_blog('MY NEWS', 'I have good news')
#        self.assertEqual(response.status_code, 201)
