from flask import Blueprint


base = Blueprint('base', __name__, template_folder='templates')


@base.route('/')
def index():
    return "Hello world"
