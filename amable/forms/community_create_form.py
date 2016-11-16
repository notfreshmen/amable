from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, FileField
from wtforms.validators import DataRequired, Email


class CommunityCreateForm(Form):
    name = StringField('Name', validators=[DataRequired("Name is required")])
    description = TextAreaField('Description')
    banner = FileField('Banner')
    thumbnail = FileField('Thumbnail')
    nsfw = BooleanField('NSFW?')
