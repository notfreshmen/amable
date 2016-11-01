from flask import Blueprint, render_template, request, flash, jsonify
from sqlalchemy import func

from amable import session

from amable.models.community import Community

from ..forms.community_search_form import CommunitySearchForm


communities = Blueprint('communities', __name__,
                        template_folder='../templates/communities')


@communities.route('/communities')
def community():
    searchForm = CommunitySearchForm()
    return render_template('communities.html', title="Search Communities", form=searchForm)


@communities.route('/communities/search', methods=['GET'])
def search_communities():
    print("got here")

    if 'community' in request.args:

        if len(request.args['community']) > 0:

            queryToSearch = request.args['community']

            communityList = session.query(Community).filter(
                func.lower(Community.name).like(func.lower(queryToSearch + "%"))).all()

            # jsonReturn = {}
            # jsonReturn.communities = []

            # for tempCommunity in communityList:
            #     jsonReturn.communities.push(tempCommunity)

            return jsonify(communities=[i.serialize for i in communityList])
        else:
            return jsonify(communities = {})
    else:
        flash("Arguments missing")
