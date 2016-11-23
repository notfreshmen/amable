from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators, HiddenField


class PostCommunityCreateForm(FlaskForm):
    text_brief = TextAreaField(
        'Post Text', [validators.Required(), validators.Length(min=1, max=160)])
    community_id = HiddenField('community')
