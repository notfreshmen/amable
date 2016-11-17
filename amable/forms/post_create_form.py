from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, HiddenField, TextAreaField
from wtforms.fields.html5 import EmailField


class PostCreateForm(FlaskForm):
    text_brief = TextAreaField('Text', [validators.Required(), validators.Length(min=1, max=160)])
    community_id = HiddenField('Community')
