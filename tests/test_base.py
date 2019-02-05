# import unittest
# import json
# from app import create_app
# from app.version1.models import blog_list, blog_id, date_and_time


# class BaseTestCase(unittest.TestCase):

#    def setUp(self):
#        app = create_app('testing')
#        app.testing = True
#        self.client = app.test_client(self)

#    def tearDown(self):
#        blog_list.clear()

#    def post_blog(self, tittle, description):

#        return self.client.post('api/v1/blog', data=json.dumps(dict(
#            blog_id=1,
#            tittle=tittle,
#            description=description,
#            time_and_date=date_and_time
#        )
#        ),
#            content_type='application/json'
#        )

#    def update_ablog(self, tittle, description):
#            blog_id=1,
#            tittle=tittle,
#            description=description,
#            time_and_date=date_and_time
#        )),
#            content_type='application/json'
#
#        )

#        def delete_one_blog(self, ):
#            return self.client.delete('api/v1/blog/1')

#        def get_one_blog(self):

#            return self.client.get('api/v1/blog/1')

#        def get_all_blogs(self):

#            return self.client.get('api/v1/blog')
