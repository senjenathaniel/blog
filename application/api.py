import pymongo
import uuid as identity


client = pymongo.MongoClient(
    "mongodb+srv://senjenathaniel-dev:SaEGXSdHxeYJmcqO@blogcluster.b9rhq.mongodb.net/blog?ssl=true&ssl_cert_reqs=CERT_NONE")


handler = client.blog
blog_posts = handler.posts


def get_posts():
    return blog_posts.find()


def get_post(key, val):
    for post in blog_posts.find({key: val}):
        return print(post)


def add_posts(posts):
    blog_posts.insert_many(posts)
    return


def add_post(post):
    blog_posts.insert_one(post)


def update_post(key, val, new_val):
    query = {key, val}
    updates = {"$set": {key, new_val}}
    blog_posts.update_one(query, updates)

    # db.example.find_one_and_update(
    #     ...     {'_id': 'userid'},
    #     ...     {'$inc': {'seq': 1}},
    #     ...     return_document=ReturnDocument.AFTER)

    # {u'_id': u'userid', u'seq': 1}
    return


def delete_post(key, val):
    blog_posts.delete_one(key, val)


def delete_all():
    blog_posts.delete_many()
