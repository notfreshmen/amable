from flask_wtf import Form
from wtforms import StringField
# from wtforms.validators import DataRequired, Email


class CommunitySearchForm(Form):
    community_name = StringField('community_name')
