from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import requests
from threading import Thread
from Hashable import Hashable
from functools import lru_cache

try: 
    import queue
except ImportError:
    import Queue as queue


app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False

parser = reqparse.RequestParser()
parser.add_argument('tags', type=str, required=True, help='Tags parameter required')
parser.add_argument('sortBy', type=str)
parser.add_argument('direction', type=str)


@lru_cache(maxsize=32) #cache results to reduce API requests
def find_tags(self, tag):
    self.str = 'http://127.0.0.1:5000/api/post?tag='+tag

    return requests.get(self.str).json()['posts']


class Home(Resource):
    def get(self):
        return jsonify({"success": True})


class GetPosts(Resource):
    def get(self):    
        self.args = parser.parse_args()
        self.tags = self.args['tags'].split(",")
        self.sortBy = self.args['sortBy']
        self.direction = self.args['direction']
        self.validSorts = ['id', 'likes', 'popularity', 'reads']
        self.validDirec = ['asc', 'desc']

        self.toHash = []
        self.result = []
        self.threads = []
        self.que = queue.Queue()
      
        
        #Error cases
        if(self.sortBy and (self.sortBy not in self.validSorts)):
            return jsonify({ "error": "sortBy parameter is invalid"})
        
        if(self.direction and (self.direction not in self.validDirec)):
            return jsonify({ "error": "direction parameter is invalid"})

        #Use multiple threads to concurently make API calls, place results into Queue
        for tag in self.tags:
            t = Thread(target=lambda q, arg1: q.put(find_tags(self, arg1)), args=(self.que, tag))
            self.threads.append(t)
            t.start()
        
        #Wait for all threads
        for i, thread in enumerate(self.threads, start=0):
            thread.join()

        #Make each post Hashable for uniquifying process
        while not self.que.empty():
            res = self.que.get()

            for post in res:
                tmp = Hashable(post)
                self.toHash.append(tmp)       

        #Uniquify post list
        self.result = list(set(self.toHash))

        #Turn Hashables back into dicts
        for i, item in enumerate(self.result, start=0):
            tmp = item.post()
            self.result[i] = tmp

        #Sort if needed
        if(self.sortBy):
            if(self.direction == 'desc'):
                self.result.sort(reverse=True, key=lambda x: x[self.sortBy])
            else:
                self.result.sort(key=lambda x: x[self.sortBy])
        else:
            self.result.sort(key=lambda x: x['id'])

        return jsonify({"posts": self.result})


api.add_resource(Home, '/api/ping')
api.add_resource(GetPosts, '/api/posts')


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)