class Hashable:

    def __init__(self, x):
        self.author = x['author']
        self.authorId = x['authorId']
        self.id = x['id']
        self.likes = x['likes']
        self.popularity = x['popularity']
        self.reads = x['reads']
        self.tags = x['tags']

    def __eq__(self, other):
        return self.author == other.author and self.authorId == other.authorId\
            and self.id == other.id and self.likes == other.likes\
            and self.popularity == other.popularity and self.reads == other.reads

    def __hash__(self):
        return hash((self.author, self.authorId, self.id, self.likes,
                    self.popularity, self.reads))

    def post(self):
        self.post = {'author': self.author, 'authorId': self.authorId,
                'id': self.id, 'likes': self.likes,
                'popularity': self.popularity, 'reads': self.reads,
                'tags': self.tags}

        return self.post