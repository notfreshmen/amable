from pprint import pprint

from flask import Blueprint
from flask import render_template, abort, request, redirect, url_for, flash

from flask_login import login_user, login_required, current_user, logout_user

from amable import session

from amable.models.user import User
from amable.models.post import Post

from amable.forms.user_create_form import UserCreateForm
from amable.forms.user_update_form import UserUpdateForm


users = Blueprint('users', __name__, template_folder='../templates')

s = session()


@users.route('/<username>')
def show(username):
    user = s.query(User).filter_by(username=username).first()

    if not user:
        return abort(404)

    posts = s.query(Post).filter_by(user_id=user.id).all()

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

        s.add(user)
        s.commit()

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
    user = s.query(User).filter_by(id=id).first()

    if user.updatable_by(current_user) is not True:
        return redirect(url_for('sessions.login'))

    form = UserUpdateForm(request.form)

    if form.validate():
        data = form.data

        if data["profile_image"] == "":
            del(data["profile_image"])

        user.update(data)

        s.commit()

        flash(u"Your account has been updated.", "success")

        return redirect(url_for('users.edit'))

    flash(form.errors)

    return redirect(url_for('users.edit'))


@users.route('/users/<id>/destroy', methods=['POST'])
@login_required
def destroy(id):
    user = s.query(User).filter_by(id=id).first()

    if user.destroyable_by(current_user) is not True:
        return redirect(url_for('sessions.login'))

    s.delete(user)
    s.commit()

    if user == current_user:
        logout_user()

    return redirect(url_for('base.index'))
