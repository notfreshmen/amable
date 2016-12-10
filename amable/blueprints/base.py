from pprint import pprint

from flask import Blueprint
from flask import render_template, flash, send_from_directory, request

from flask_login import current_user

from amable.forms.user_create_form import UserCreateForm
from amable.forms.post_create_form import PostCreateForm

from amable import session

from amable.services.feed_service import FeedService
from ..forms.login_form import LoginForm


base = Blueprint('base', __name__, template_folder='../templates/base')


@base.route('/')
def index():
    if current_user.is_authenticated:
        form = PostCreateForm()
        user_communities = current_user.get_communities()
        form.community_select.choices = [
            (c.id, c.name) for c in user_communities]

        service = FeedService(user=current_user)

        if request.args.get('feed') is None or request.args.get('feed') == 'communities':
            posts = service.communities()
            feed_type = 'communities'
        elif request.args.get('feed') == 'users':
            posts = service.users()
            feed_type = 'users'
        else:
            posts = service.top()
            feed_type = 'top'

        return render_template('index.html', posts=posts, form=form, feed=service, feed_type=feed_type)
    login_form = LoginForm()
    return render_template('index.html',
                           form=login_form,
                           title="Amable - Login")


@base.route('/ui')
def ui():
    return render_template('ui.html', title="UI Guide")


@base.route('/uploads/<path:path>')
def serve_upload(path):
    print(path)

    return send_from_directory('uploads/', path)
