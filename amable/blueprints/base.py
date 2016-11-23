from flask import Blueprint
from flask import render_template, flash, send_from_directory
from amable.forms.user_create_form import UserCreateForm
from amable.forms.post_create_form import PostCreateForm


base = Blueprint('base', __name__, template_folder='../templates/base')


@base.route('/')
def index():
    form = PostCreateForm()
    return render_template('index.html', form=form)


@base.route('/ui')
def ui():
    return render_template('ui.html', title="UI Guide")


@base.route('/uploads/<path:path>')
def serve_upload(path):
    print(path)

    return send_from_directory('uploads/', path)
