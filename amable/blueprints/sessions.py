from flask import Blueprint
from flask import render_template, redirect, request
from flask_login import login_user

from amable.models.user import User
from amable import session, login_manager

from ..forms.login_form import LoginForm

sessions = Blueprint('sessions', __name__,
                     template_folder='../templates/sessions')


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).first()


@sessions.route('/login', methods=['GET'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


@sessions.route('/sessions/create', methods=['POST'])
def create():
    # email 'variable' is the column. request.form['email'] is the post data
    user = session.query(User).filter_by(email=request.form["email"]).first()
    print(user.password)

    # Does the user exist from the query done above?
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
