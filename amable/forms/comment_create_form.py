from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, HiddenField
from wtforms.validators import Optional

class CommentCreateForm(FlaskForm):
	parent = HiddenField('Parent Comment', [Optional()])
	content = TextAreaField('Comment Content')
	post = HiddenField('Post', [Optional()])
	next = HiddenField('Next')

