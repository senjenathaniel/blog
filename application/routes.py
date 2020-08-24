from flask import current_app as app
from flask import render_template, redirect, request, url_for
import sqlite3 as sql

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

from . db_functions import get_posts, delete_post, get_single_post, get_notes
from . forms import CreatePost

"""
    APPLICATION ROUTES
"""


@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", title="senjenathaniel blog", posts=posts)


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):

    if request.method == "POST":
        with get_single_post(post_id) as post:
            print(post)
    else:
        return render_template("update.html", post=post)


@app.route("/delete/<post_id>")
def delete(post_id):
    try:
        delete_post(post_id)
    except Exception as e:
        print(e)

    return "admin"


@app.route("/admin")
def admin():
    posts = get_posts()

    return render_template("admin.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
def create():
    form = CreatePost()

    if form.validate_on_submit():
        try:
            with sql.connect("database.db") as conn:
                c = conn.cursor()
                c.execute(
                    "INSERT INTO posts (title, content, category, date_created) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
                    (form.blog_title, form.blog_category, form.blog_content),
                )
                conn.commit()

        except Exception as e:
            print("There was an error: " + e)
            conn.rollback()
        finally:
            conn.close()
            return redirect(url_for("index.html", msg="Record added Successfully"))

    print(form.blog_title)
    return render_template("create_post.html", form=form)


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
