from flask import current_app as app
from flask import render_template, redirect, request, url_for, flash
import sqlite3 as sql
import uuid

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

from . forms import CreatePost
from . api import get_posts, get_post, update_post, delete_post, add_post, get_one


UID = uuid.uuid4()

"""
    APPLICATION ROUTES
"""


@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", title="senjenathaniel blog", posts=posts)


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):
    form = CreatePost()
    post = get_post(post_id)

#     if request.method == "POST":
#         with get_single_post(post_id) as post:
#             print(post)
#     else:
    return render_template("update.html", post=post, form=form)


@app.route("/delete/<post_id>")
def delete(post_id):
    try:
        delete_post(post_id)
        return render_template("success.html")
    except Exception as e:
        print(e)

    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html", posts=get_posts())


@app.route("/create", methods=["GET", "POST"])
def create():
    form = CreatePost()

    title = form.blog_title.data
    body = form.blog_content.data

    post = {
        "_id": UID,
        "userId": 1,
        "id": 100,
        "title": title,
        "body": body
    }

    if request.method == "POST":
        try:
            if form.validate() == False:
                flash('All fields are required.')
                return render_template('create.html', form=form)
            else:
                add_post(post)
                return render_template('success.html')
        except Exception as e:
            print(e)
    else:
        pass

    return render_template('create.html', form=form)


@app.route("/single_post/<post_id>")
def post(post_id):
    post = get_post(post_id)
    print(post)
    return post


""" 
     Login and Register
"""


@app.route("/login", methods=("GET", "POST"))
def login():
    return "login"
