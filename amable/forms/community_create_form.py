from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, FileField
from wtforms.validators import DataRequired, Email


class CommunityCreateForm(Form):
    name = StringField('name', validators=[DataRequired("Name is required")])
    description = TextAreaField('description')
    banner = FileField('banner')
    thumbnail = FileField('thumbnail')
    nsfw = BooleanField('nsfw')
