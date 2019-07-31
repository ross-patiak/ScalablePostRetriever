import random
import ulid
import json
from Post import Post
from faker import Faker
fake = Faker()

def generate_all_posts():
        unique_names = set("")
        unique_users = []
        posts = []

        x = 0
        while len(unique_names) != 200:
                name = {fake.name()}

                if name.difference(unique_names) == name:
                        name = name.pop()
                        unique_names.add(name)
                        unique_users.append({'author': name, 'authorId': x+1})

                x = x + 1

        for x in range(1000):
            rand_index = random.randint(0, len(unique_users) - 1)
            author = unique_users[rand_index]['author']
            authorId = unique_users[rand_index]['authorId']

            posts.append(Post.generate_rand(author, authorId))

        return posts

all_posts = generate_all_posts()
F = open("all-posts.txt", "w")
tmp = json.dumps({'posts': all_posts})
F.write(tmp)
F.close()