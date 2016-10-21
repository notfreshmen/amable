from flask import Blueprint
from flask import render_template, redirect, request

from amable import app, session
from amable.models.user import User

from amable.utils.password import hash_password, check_password

sessions = Blueprint('sessions', __name__, template_folder='../templates/sessions')


@sessions.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@sessions.route('/sessions/create', methods=['POST'])
def create():
    #email 'variable' is the column. request.form['email'] is the post data
    user = session.query(User).filter_by(email=request.form["email"]).first()
    print(user.password)
    if user is None:
        return redirect('/login')
    if check_password(user.password, request.form["password"]):
        return redirect("/")
    else:
        return redirect('/login')