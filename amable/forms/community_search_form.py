from flask_wtf import FlaskForm
from wtforms import StringField
# from wtforms.validators import DataRequired, Email


class CommunitySearchForm(FlaskForm):
    community_name = StringField('community_name')
