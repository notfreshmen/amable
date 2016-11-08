from flask import Blueprint
from flask import render_template, flash


base = Blueprint('base', __name__, template_folder='../templates/base')


@base.route('/')
def index():
    return render_template('index.html', title="Amable Home")


@base.route('/ui')
def ui():
    return render_template('ui.html', title="UI Guide")
