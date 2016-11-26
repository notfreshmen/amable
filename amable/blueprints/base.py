from flask import Blueprint
from flask import render_template, flash, send_from_directory

from flask_login import current_user

from amable.forms.user_create_form import UserCreateForm
from amable.forms.post_create_form import PostCreateForm
from amable import session

from amable.models.post import Post


base = Blueprint('base', __name__, template_folder='../templates/base')


@base.route('/')
def index():
    if current_user.is_authenticated:
        form = PostCreateForm()
        user_communities = current_user.get_communities()
        form.community_select.choices = [
            (c.id, c.name) for c in user_communities]

        posts = Post.for_user(current_user)

        return render_template('index.html', posts=posts, form=form)

    return render_template('index.html')


@base.route('/ui')
def ui():
    return render_template('ui.html', title="UI Guide")


@base.route('/uploads/<path:path>')
def serve_upload(path):
    print(path)

    return send_from_directory('uploads/', path)
