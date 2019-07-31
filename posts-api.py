from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import requests, json, random
from threading import Thread
from Post import Post


app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False

parser = reqparse.RequestParser()
parser.add_argument('tag', type=str, required=True, help='Tags parameter required')

F = open("all-posts.txt", "r")
postList = json.loads(''.join(F.readlines()))
F.close()

class AllPosts(Resource):
    def get(self):
        return postList


class GetPost(Resource):
    def get(self):
        self.args = parser.parse_args()
        self.tag = self.args['tag']

        if(self.tag not in Post.get_valid_tags()):
            return {"error": "Tag not valid"}

        self.posts = requests.get('http://127.0.0.1:5000/api/all').json()['posts']

        self.posts = list(filter(lambda x: self.tag in x['tags'], self.posts))

        return jsonify({"posts": self.posts})


api.add_resource(AllPosts, '/api/all')
api.add_resource(GetPost, '/api/post')


if __name__ == '__main__':
    app.run(debug=True)