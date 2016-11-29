from pprint import pprint

from flask import Blueprint, request, redirect, url_for, flash, jsonify, render_template

from flask_login import login_required, current_user

from amable import session, csrf

from amable.models.post import Post
from amable.models.post_upvote import PostUpvote
from amable.models.community import Community
from amable.forms.post_create_form import PostCreateForm

from amable.utils.misc import flash_errors


posts = Blueprint('posts', __name__, template_folder='../templates/posts')


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
    post = session.query(Post).filter_by(id=id).first()

    if post.destroyable_by(current_user):
        session.delete(post)
        session.commit()
    else:
        flash("Can't delete a post you didn't create")

    return redirect(request.form["redirect_to"])


@posts.route('/posts/<id>/upvote', methods=['GET'])
@login_required
def upvote_post(id):
    returnDict = {}
    # First lets get the post were upvoting
    post = session.query(Post).filter_by(id=id).first()

    # Check to see user hasn't already upvoted
    if not current_user.has_upvoted_post(post):
        returnDict['success'] = True
        pu = PostUpvote(post, current_user)

        # Add the new post upvote
        session.add(pu)
        session.commit()
    else:
        returnDict['success'] = False
        # flash("User has already upvoted post")

    return jsonify(**returnDict)


@posts.route('/posts/<id>/downvote', methods=['GET'])
@login_required
def downvote_post(id):
    returnDict = {}
    # First lets get the post were upvoting
    pu = session.query(PostUpvote).filter_by(
        post_id=id, user_id=current_user.id).first()

    # Check to see user has actually upvoted
    if pu is not None:
        returnDict['success'] = True

        # Delete the post upvote
        session.delete(pu)
        session.commit()
    else:
        returnDict['success'] = False

    return jsonify(**returnDict)
