from flask import Blueprint
from flask import render_template, abort, request, redirect, url_for, flash

from amable import session

from amable.models.user import User
from amable.models.post import Post

from amable.forms.user_create_form import UserCreateForm
from amable.forms.user_update_form import UserUpdateForm


users = Blueprint('users', __name__, template_folder='../templates/users')

s = session()


@users.route('/<username>')
def show(username):
    user = s.query(User).filter_by(username=username).first()

    if not user:
        return abort(404)

    posts = s.query(Post).filter_by(user_id=user.id).all()

    return render_template('show.html', user=user, posts=posts)


@users.route('/join')
def new():
    return render_template('new.html', form=UserCreateForm())


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

        # log in here at some point

        return redirect(url_for('base.index'))

    return render_template('new.html', form=form)


@users.route('/account')
def edit():
    user = s.query(User).filter_by(username='ethan').first()

    form = UserUpdateForm(obj=user)

    return render_template('edit.html', current_user=user, form=form)


@users.route('/users/<id>/update', methods=['POST'])
def update(id):
    print('update hit')
    user = s.query(User).filter_by(id=id).first()

    form = UserUpdateForm(request.form)

    if form.validate():
        data = form.data

        # Don't set the profile_image to None if there's no input
        if data["profile_image"] == "":
            del(data["profile_image"])

        user.update(data)

        s.commit()

        return redirect(url_for('users.edit'))

    print('not validated')

    flash(form.errors)

    return redirect(url_for('users.edit'))


@users.route('/users/<id>/destroy', methods=['POST'])
def destroy(id):
    user = s.query(User).filter_by(id=id).first()

    s.delete(user)
    s.commit()

    return redirect(url_for('base.index'))
