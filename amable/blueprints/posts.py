from pprint import pprint

from flask import Blueprint
from flask import render_template, abort, request, redirect, url_for, flash

from flask_login import login_user, login_required, current_user, logout_user

from amable import session, csrf

from amable.models.user import User
from amable.models.post import Post
from amable.models.community import Community
from amable.forms.post_create_form import PostCreateForm


posts = Blueprint('posts', __name__, template_folder='../templates/posts')

s = session()


@login_required
@posts.route('/posts', methods=['POST'])
def create():
    form = PostCreateForm(request.form)
    pprint(current_user)
    pprint(request.form)
    if form.validate():
        post = Post(
            text_brief=form.text_brief.data,
            text_long=None,
            image_url=None,
            user_id=current_user.id,
            community_id=form.community_id.data
        )

        s.add(post)
        s.commit()

        flash(u"Post Successfully Created", "success")
    else:
        flash(u"Post failed", "error")

    return redirect(url_for('base.index'))

#    if form.validate():
 #       user = User(
  #          username=form.username.data,
   #         email=form.email.data,
    #        name=form.name.data,
     ##  )

       # s.add(user)
       # s.commit()

        #login_user(user)

        #return redirect(url_for('base.index'))

   # return render_template('new.html', form=form)
   
@csrf.exempt
@posts.route('/posts/<id>/destroy', methods=['POST'])
@login_required
def destroy(id):
    post = s.query(Post).filter_by(id=id).first()
    
    s.delete(post)
    s.commit()

    return redirect(request.form["redirect_to"])

