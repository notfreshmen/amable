from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, choices, HiddenField
# IntegerField, FileField, BooleanField, TextAreaField, validators
# from wtforms.fields.html5 import EmailField, DateField


class PostReportForm(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Report Content')
    category = SelectField('Category of Report', choices[
        ('offensive', 'Offensive'),
        ('norelevant', 'Not Relevant'),
        ('other', 'Other')])
    post = HiddenField('Post')
