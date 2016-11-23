from pprint import pprint

from flask import Blueprint
from flask import render_template, abort, request, redirect, url_for, flash

from flask_login import login_user, login_required, current_user, logout_user

from amable import session, csrf

from amable.models.user import User
from amable.models.post import Post
from amable.models.community import Community
from amable.forms.post_create_form import PostCreateForm
from amable.forms.post_community_create_form import PostCommunityCreateForm
from wtforms.validators import ValidationError

from amable.utils.misc import flash_errors


posts = Blueprint('posts', __name__, template_folder='../templates/posts')

s = session()


@posts.route('/posts', methods=['POST'])
@login_required
def create():
    community = None  # This will be just a filler object for our community

    # Get the form data
    form = PostCreateForm(request.form)

    # Set the valid community choices
    form.community_select.choices = [
        (c.id, c.name) for c in current_user.get_communities()]

    if form.validate():

        # We need to get the community to pass through to post
        # constructor

        # First we check if there was the hidden field, or if
        # it was a select box
        if form.community_id.data is not "":  # Hidden Field
            community = session.query(Community).filter_by(
                id=int(form.community_id.data)).first()
        elif form.community_select is not None:  # Select Box
            community = session.query(Community).filter_by(
                id=int(form.community_select.data)).first()

        # Create the post object
        post = Post(
            text_brief=form.text_brief.data,
            text_long=None,
            image_url=None,
            user=current_user,
            community=community
        )

        # Add to the session and commit to the database
        session.add(post)
        session.commit()

        flash(u"Post Successfully Created", "success")
    else:
        pprint(form.errors)
        flash(u"Post failed", "error")

        # lets also flash the errors
        flash_errors(form)

    return redirect(url_for('communities.show', permalink=community.permalink))


@csrf.exempt
@posts.route('/posts/<id>/destroy', methods=['POST'])
@login_required
def destroy(id):
    post = s.query(Post).filter_by(id=id).first()
    s.delete(post)
    s.commit()
    return redirect(request.form["redirect_to"])
