from flask_restful import Resource
from flask import make_response, jsonify, request
from app.version1.models import MyBlogModel
# import datetime
# import time


class MyBlog(Resource, MyBlogModel):
    def __init__(self):
        self.db = MyBlogModel()

    def post(self):
            data = request.get_json()
            tittle = data['tittle']
            description = data['description']
            if not tittle:
                return jsonify({"message": "field empty"})
            elif not description:
                return jsonify({"message": "field empty"})
            elif isinstance(tittle, int):
                return jsonify({"message": "should be a string"})
            elif isinstance(description, int):
                return jsonify({"message": "should be a string"})
            respo = self.db.add_blog(tittle, description)
            return make_response(jsonify({
                "message": 'ok',
                "my_blog": respo

            }), 201)
        # return jsonify({'message': 'Inverid or missing fields'})

    def get(self):
        all_blogs = self.db.get_blogs()
        return make_response(jsonify({
            "message": 'ok',
            "my_blog": all_blogs

        }), 200)


class SingleBlog(MyBlog):

    def get(self, blog_id):
        ablog = self.db.get_one(blog_id)
        return ablog

    def put(self, blog_id):
        updated_blog = self.db.update_blog(blog_id)
        return updated_blog

    def delete(self, blog_id):
        deleted_blog = self.db.delete_one(blog_id)
        return deleted_blog
