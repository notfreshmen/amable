from flask import Blueprint
from flask import render_template


communities = Blueprint('communities', __name__,
                        template_folder='../templates/communities')


@communities.route('/communities')
def community():
    return render_template('communities.html')
