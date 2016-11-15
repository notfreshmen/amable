from flask_wtf import FlaskForm
from wtforms import FileField
# from wtforms.validators import DataRequired, Email


class FileTestForm(FlaskForm):
    file_field = FileField('fileField')
