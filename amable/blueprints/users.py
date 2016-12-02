from pprint import pprint

import os

from flask import Blueprint
from flask import render_template, abort, request, redirect, url_for, flash

from flask_login import login_user, login_required, current_user, logout_user

from werkzeug.utils import secure_filename

from amable import session

from amable.models.user import User
from amable.models.post import Post
from amable.models.follower import Follower

from amable.forms.user_create_form import UserCreateForm
from amable.forms.user_update_form import UserUpdateForm

from sqlalchemy import desc
from sqlalchemy import asc

users = Blueprint('users', __name__, template_folder='../templates')


@users.route('/<username>')
@login_required
def show(username):
    user = session.query(User).filter_by(username=username).first()

    if not user:
        return abort(404)

    posts = session.query(Post).filter_by(user_id=user.id).order_by(
        desc(Post.date_created)).all()

    return render_template('users/show.html', user=user, posts=posts)


@users.route('/join')
def new():
    return render_template('users/new.html', form=UserCreateForm())


@users.route('/users', methods=['POST'])
def create():
    form = UserCreateForm(request.form)

    if form.validate():
        user = User(
            username=form.username.data,
            email=form.email.data,
            name=form.name.data,
            password=form.password.data
        )

        session.add(user)
        session.commit()

        login_user(user)

        return redirect(url_for('base.index'))

    return render_template('users/new.html', form=form)


@users.route('/account')
@login_required
def edit():
    form = UserUpdateForm(obj=current_user)

    return render_template('users/edit.html', form=form)


@users.route('/users/<id>/update', methods=['POST'])
@login_required
def update(id):
    user = session.query(User).filter_by(id=id).first()

    if user.updatable_by(current_user) is not True:
        return redirect(url_for('sessions.login'))

    form = UserUpdateForm(request.form)

    if form.validate():
        data = form.data

        if request.files['profile_image']:
            filename = secure_filename(request.files['profile_image'].filename)

            if not os.path.exists('./amable/uploads/avatars/' + str(user.id)):
                os.makedirs('./amable/uploads/avatars/' + str(user.id))

            request.files['profile_image'].save(
                './amable/uploads/avatars/' + str(user.id) + '/' + filename)

            user.profile_image = '/uploads/avatars/' + \
                str(user.id) + '/' + filename

        user.set_password(data['password'])

        del(data['profile_image'])
        del(data['password'])

        user.update(data)

        session.commit()

        flash(u"Your account has been updated.", "success")

        return redirect(url_for('users.edit'))

    flash(form.errors)

    return redirect(url_for('users.edit'))


@users.route('/users/<id>/destroy', methods=['POST'])
@login_required
def destroy(id):
    user = session.query(User).filter_by(id=id).first()

    if user.destroyable_by(current_user) is not True:
        return redirect(url_for('sessions.login'))

    user.active = False
    session.commit()

    if user == current_user:
        logout_user()

    return redirect(url_for('base.index'))

@users.route('/follow/<id>', methods=['GET'])
@login_required
def follow(id):
    returnDict = {}

    user_to_follow = session.query(User).filter_by(id=id).first()

    if user_to_follow is not None:
        returnDict['success'] = True
        follower = Follower(source_user=current_user, target_user=user_to_follow)
        session.add(follower)
        session.commit()
    else:
        returnDict['success'] = False

    return redirect(**returnDict)

