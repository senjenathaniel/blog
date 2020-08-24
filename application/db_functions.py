import sqlite3
from flask import Flask, render_template, url_for, redirect, request
import sqlite3 as sql

"""
    DATABASE FUNCITONS
"""


def get_single_post(id):
    try:
        with sql.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM posts WHERE id = ?', id)

            post = c.fetchone()
            conn.commit()

            return post
    except sqlite3.Error as e:
        print("Failed: ", e)
    finally:
        if (conn):
            conn.close()


def get_notes():
    # Not implemented just yet
    try:
        with sql.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM notes')

            posts = c.fetchall()
            conn.commit()

            return posts
    except sqlite3.Error as e:
        print("Failed: ", e)
    finally:
        if (conn):
            conn.close()


def get_posts():
    try:
        with sql.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM posts')

            posts = c.fetchall()
            conn.commit()

            return posts
    except sqlite3.Error as e:
        print("Failed: ", e)
    finally:
        if (conn):
            conn.close()


def update_post(id, content):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Deleting single record now
        c.execute("UPDATE from posts where id = ?", id)
        conn.commit()
        print("post Update successfully ")
        c.close()

    except sqlite3.Error as e:
        print("Failed to update post: ", e)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")


def delete_post(post_id):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Deleting single record now
        c.execute("DELETE from posts where id = ?", post_id)
        conn.commit()
        print("Record deleted successfully ")
        c.close()

    except sqlite3.Error as e:
        print("Failed to delete record: ", e)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")
