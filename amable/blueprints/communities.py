from flask import Blueprint, render_template, request, flash, jsonify, abort
from flask_login import login_required

from sqlalchemy import func
from sqlalchemy.orm import joinedload

from amable import session

from amable.models.community import Community
from amable.models.post import Post

from amable.forms.community_search_form import CommunitySearchForm


communities = Blueprint('communities', __name__,
                        template_folder='../templates')

s = session()


@communities.route('/communities')
def index():
    communities = s.query(Community).all()

    print(communities)

    return render_template('communities/index.html',
                           title="Communities",
                           communities=communities,
                           form=CommunitySearchForm())


@communities.route('/communities/search', methods=['GET'])
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


@communities.route('/communities/<permalink>')
@login_required
def show(permalink):
    community = s.query(Community).filter_by(permalink=permalink).first()

    if not community:
        return abort(404)

    posts = s.query(Post).filter_by(community_id=community.id).all()

    return render_template('communities/show.html',
                           community=community,
                           posts=posts)
