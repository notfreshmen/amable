from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired("Email is Required"), Email("Email is not valid format")])
    password = PasswordField('password', validators=[DataRequired("Password is required")])
