from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class CreatePost(FlaskForm):
    blog_title = TextField('Blog Title', [DataRequired()])
    blog_content = TextAreaField('Content', [DataRequired(), Length(
        min=100, message="Your content is too little. Write some more!")])
    submit = SubmitField('Create Post')
