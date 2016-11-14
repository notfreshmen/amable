from flask import Blueprint
from flask import render_template, flash, send_from_directory


base = Blueprint('base', __name__, template_folder='../templates/base')


@base.route('/')
def index():
    return render_template('index.html')


@base.route('/ui')
def ui():
    return render_template('ui.html', title="UI Guide")


@base.route('/uploads/<path:path>')
def serve_upload(path):
    print(path)

    return send_from_directory('uploads/', path)
