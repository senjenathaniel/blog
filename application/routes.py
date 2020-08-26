from flask import current_app as app
from flask import render_template, redirect, request, url_for
import sqlite3 as sql
import uuid as identity

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

from . forms import CreatePost
from . api import get_posts, get_post, update_post, delete_post, add_post

"""
    APPLICATION ROUTES
"""


@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", title="senjenathaniel blog", posts=posts)


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):
    pass

    post = get_post("id", post_id)

#     if request.method == "POST":
#         with get_single_post(post_id) as post:
#             print(post)
#     else:
    return render_template("update.html", post=post)


@app.route("/delete/<post_id>")
def delete(post_id):
    # try:
    #     delete_post(post_id)
    # except Exception as e:
    #     print(e)

    return


@app.route("/admin")
def admin():
    posts = get_posts()

    return render_template("admin.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
def create():
    pass
    form = CreatePost()

    post = {
        "_id": identity.uuid4(),
        "userId": 1,
        "id": 100,
        "title": form.blog_title,
        "body": form.blog_content
    }
    if form.validate_on_submit():
        try:
            add_post(post)
            redirect(url_for('index'))
        except Exception as e:
            print("There was an error: " + e)

    # return redirect(url_for("index"))

    return render_template("create.html", form=form)


@app.route("/post", methods=["GET", "POST"])
def post():
    return "post"


""" 
     Login and Register
"""


@app.route("/login", methods=("GET", "POST"))
def login():
    return "login"


# class LoginForm(FlaskForm):
#     """Login form."""

#     username = StringField("Username", [DataRequired()])
#     password = PasswordField("Passwowrd", [DataRequired()])
#     submit = SubmitField("Submit")
