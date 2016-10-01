from flask import Blueprint
from flask import render_template


users = Blueprint('users', __name__, template_folder='../templates/users')


@users.route('/<username>')
def users_show(username):
    return render_template('show.html', username=username)


@users.route('/join')
def users_new():
    return render_template('new.html')


@users.route('/users', methods=['POST'])
def users_create():
    return "Create a user"


@users.route('/account')
def users_edit():
    return render_template('edit.html')


@users.route('/users/<id>', methods=['PATCH'])
def users_update():
    return "Update a user"


@users.route('/users/<id>', methods=['DELETE'])
def users_destroy():
    return "Destroy a user"
