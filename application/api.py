import pymongo
import uuid as identity


client = pymongo.MongoClient(
    "mongodb+srv://senjenathaniel:4BXBpEdw9Fmf@blogcluster.b9rhq.mongodb.net/blog?ssl=true&ssl_cert_reqs=CERT_NONE")


posts = client.blog.posts


def get_one():
    return posts.find_one()


def get_posts():
    return posts.find()


def get_post(val):
    for post in posts.find({"id": val}):
        return post


def add_posts(posts):
    posts.insert_many(posts)
    return


def add_post(post):
    posts.insert_one(post)


def update_post(val, new_val):
    query = {"id", val}
    updates = {"$set": {"id", new_val}}
    posts.update_one(query, updates)

    # db.example.find_one_and_update(
    #     ...     {'_id': 'userid'},
    #     ...     {'$inc': {'seq': 1}},
    #     ...     return_document=ReturnDocument.AFTER)

    # {u'_id': u'userid', u'seq': 1}
    return


def delete_post(val):
    try:
        posts.delete_many({"id": val})
        print("Deletion succesful")
    except Exception as e:
        print(str(e))
    return
