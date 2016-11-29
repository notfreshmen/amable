from pprint import pprint

from flask import Blueprint, request, redirect, url_for, flash, jsonify, render_template

from flask_login import login_required, current_user

from amable import session, csrf

from amable.models.comment import Comment
from amable.models.post import Post
from amable.models.post_upvote import PostUpvote
from amable.models.community import Community

from amable.forms.comment_create_form import CommentCreateForm

from amable.utils.misc import flash_errors

import sys


comments = Blueprint('comments', __name__,
                     template_folder='../templates/comments')

# Coming into this there needs to be one of two things.
# Either we need the parent comment id, OR
# we need the post id. If we get the post_id we know
# that it is a root (level 0) comment.


@comments.route('/comments/new', methods=['POST'])
@csrf.exempt
@login_required
def create():
    pprint("Got to create()")
    # return render_template('index.html')
    comment = None
    parent_post = None

    form = CommentCreateForm(request.form, csrf_enabled=False)

    if form.validate():  # Valid data

        # We need to get the post that the com
        # session.query(Post)

        if form.parent.data is not None:
            print("got heeee")

            # We need to get the post that the com
            parent_comment = session.query(Comment).filter_by(
                id=int(form.parent.data)).first()

            pprint("Parent Comment : %r" % parent_comment)

            parent_post = parent_comment.post

            pprint("Parent Post : %r" % parent_post)

            pprint("Comment Data : %s" % form.content.data)
            # pprint("Comment Data2 : %s" % request.form['content'])

            comment = Comment(content=form.content.data,
                              user=current_user,
                              post=parent_post,
                              parent=parent_comment)

            pprint("hey" + str(comment))

        elif form.post_id.data is not None:
            print("got thereeeee")
            # Lets get the post
            parent_post = session.query(Post).filter_by(
                id=int(form.post_id.data)).first()

            comment = Comment(content=form.content.data,
                              user=current_user,
                              post=parent_post)
        else:
            print ('yollllllllll')

        try:
            pprint(comment)
            session.add(comment)
            session.commit()
        except:
            print("Unexpected Error : %s" % sys.exc_info()[0])

        return redirect(url_for('communities.show',
                                permalink=parent_post.community.permalink))

    else:
        pprint(form.errors)
        flash_errors(form)

        return redirect(url_for('base.index'))
