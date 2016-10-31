from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(
        "Email is Required"), Email("Email is not valid format")])
    password = StringField('password', validators=[
                           DataRequired("Password is required")])
