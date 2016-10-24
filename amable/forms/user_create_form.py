from wtforms import Form, StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField

class UserCreateForm(Form):
    username = StringField('Username', [validators.Required(), validators.Length(min=3, max=25)])
    email = EmailField('Email', [validators.Required(), validators.Email()])
    name = StringField('Name', [validators.Required()])
    password = PasswordField('Password', [validators.Required(), validators.EqualTo('password_confirmation', message='Passwords must match')])
    password_confirmation = PasswordField('Password confirmation', [validators.Required()])
