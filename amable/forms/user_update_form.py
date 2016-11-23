from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import Form, StringField, PasswordField, TextAreaField, validators
from wtforms.fields.html5 import EmailField, DateField


class UserUpdateForm(FlaskForm):
    username = StringField('Username', [validators.Required(), validators.Length(min=3, max=25)])
    email = EmailField('Email', [validators.Required(), validators.Email()])
    name = StringField('Name', [validators.Required()])
    bio = TextAreaField('Biography')
    location = StringField('Location')
    website = StringField('Website')
    phone = StringField('Phone number')
    profile_image = FileField('Profile image')
    password = PasswordField('Password', [validators.EqualTo('password_confirmation', message='Passwords must match.')])
    password_confirmation = PasswordField('Password confirmation',)
