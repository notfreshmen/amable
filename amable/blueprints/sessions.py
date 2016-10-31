from flask import Blueprint
from flask import render_template, redirect, request
from flask_login import login_user

from amable import app, session
from amable.models.user import User

from amable.utils.password import hash_password, check_password

sessions = Blueprint('sessions', __name__,
                     template_folder='../templates/sessions')


@sessions.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@sessions.route('/sessions/create', methods=['POST'])
def create():
    # email 'variable' is the column. request.form['email'] is the post data
    user = session.query(User).filter_by(email=request.form["email"]).first()
    print(user.password)
    if user is None:
        return redirect('/login')

    form = LoginForm()
    if form.validate_on_submit():
        if check_password(user, request.form["password"]):
            login_user(user)
            flask.flash('Logged in successfully.')
            return redirect("/")
    else:
        return redirect('/login')
