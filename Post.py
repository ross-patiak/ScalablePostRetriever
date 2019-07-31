import requests
import asyncio
import random
import ulid


class Post:

    def __init__(self, author, authorId, id, likes, popularity, reads, tags):
        self.author = author
        self.authorId = authorId
        self.id = id
        self.likes = likes
        self.popularity = popularity
        self.reads = reads
        self.tags = tags

    def generate(self):
        return {"author": self.author,
                "authorId": self.authorId,
                "id": self.id,
                "likes": self.likes,
                "popularity": self.popularity,
                "reads": self.reads,
                "tags": self.tags}

    def get_valid_tags():
        return ['science', 'health', 'tech', 'history', 'fashion']
    
    def generate_tags():
        valid_tags = Post.get_valid_tags()
        tags = set("")

        while len(list(tags)) != random.randint(1, len(valid_tags)+1): #pick how many tags
            rand_index = random.randint(0, len(valid_tags) - 1) #pick a random tag
            picked_tag = {valid_tags[rand_index]}

            if picked_tag.difference(tags) == picked_tag: #validate that it is not already a tag
                tags.add(picked_tag.pop())

        return list(tags)

    def generate_rand(author, authorId):
        likes = random.randint(0, 20000)
        reads = random.randint(0, 10000) + likes
        popularity = round(random.random(),2)
        id = ulid.new().str
        tags = Post.generate_tags()
        
        return Post(author, authorId, id, likes, popularity, reads, tags).generate()

# print(Post.generate_rand())