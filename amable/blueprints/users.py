from flask import Blueprint
from flask import render_template, abort, request, redirect, url_for

from amable import session

from amable.models.user import User
from amable.models.post import Post

from amable.forms.user_create_form import UserCreateForm


users = Blueprint('users', __name__, template_folder='../templates/users')

db = session()


@users.route('/<username>')
def show(username):
    user = db.query(User).filter_by(username=username).first()

    if not user:
        return abort(404)

    posts = db.query(Post).filter_by(user_id=user.id).all()

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

        db.commit()

        # log in here at some point

        return redirect(url_for('base.index'))

    return render_template('new.html', form=form)


@users.route('/account')
def edit():
    return render_template('edit.html')


@users.route('/users/<id>', methods=['PATCH'])
def update():
    return "Update a user"


@users.route('/users/<id>', methods=['DELETE'])
def destroy():
    return "Destroy a user"
