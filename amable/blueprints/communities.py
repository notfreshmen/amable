from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from amable import session

from amable.models.community import Community

from amable.forms.community_search_form import CommunitySearchForm


communities = Blueprint('communities', __name__,
                        template_folder='../templates')

s = session()


@communities.route('/communities')
@login_required
def index():
    return render_template('communities/search.html', title="Search Communities", form=CommunitySearchForm())


@communities.route('/communities/search', methods=['GET'])
@login_required
def search():
    if 'community' in request.args:

        if len(request.args['community']) > 0:

            queryToSearch = request.args['community']

            communityList = session.query(Community).filter(
                func.lower(Community.name).like(func.lower(queryToSearch + "%"))).all()

            return jsonify(communities=[i.serialize for i in communityList])
        else:
            return jsonify(communities={})
    else:
        flash("Arguments missing")

@login_required
@communities.route('/communities/<id>')
def show(id):
    community = s.query(Community).filter_by(id=id).first()

    return render_template('communities/show.html', community=community)
