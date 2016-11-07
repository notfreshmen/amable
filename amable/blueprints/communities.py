from flask import Blueprint, render_template, request, flash, jsonify
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from amable import session

from amable.models.community import Community

from amable.forms.community_search_form import CommunitySearchForm


communities = Blueprint('communities', __name__, template_folder='../templates/communities')


@communities.route('/communities')
def index():
    return render_template('search.html', title="Search Communities", form=CommunitySearchForm())


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


@communities.route('/communities/<id>')
def show(id):
    # First lets make sure the community exists
    tempCommunity = session.query(Community).options(joinedload('posts')).filter_by(id=id).first()
    # print("temp com posts" + tempCommunity.posts[0].user.name)
    print ("")

    if tempCommunity is None:
        print("no")
        return "no"
    else:

        # Here we have to build the comment tree. This way
        # when we pass through the comments it is just an
        # array w/ levels.
        # Here we go...
        commentList = []
        commentRaw = tempCommunity.posts[0]
        print(commentRaw)


        return render_template('show.html', title="Amable - " + tempCommunity.name, community=tempCommunity.serialize, posts = tempCommunity.posts)
