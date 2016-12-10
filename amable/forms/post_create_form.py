from flask_wtf import FlaskForm
from wtforms import validators, HiddenField, TextAreaField, SelectField
from wtforms.validators import Optional


class PostCreateForm(FlaskForm):
    text_brief = TextAreaField(
        'Make Post', [validators.Required(), validators.Length(min=1, max=160)])
    community_select = SelectField(
        'Select Community', [Optional()], coerce=int)
    community_id = HiddenField('Community', [Optional()])
