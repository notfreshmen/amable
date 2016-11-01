from flask import Blueprint, render_template, request, flash, jsonify

from amable import session

from amable.models.community import Community


communities = Blueprint('communities', __name__,
                        template_folder='../templates/communities')


@communities.route('/communities')
def community():
    return render_template('communities.html', title="View Communities")

@communities.route('/communities/search', methods=['GET'])
def search_communities():
    print("got here")

    if 'community' in request.args:
        print("request form " + request.args['community'])

        queryToSearch = request.args['community']

        print("query to serach " + queryToSearch)

        communityList = session.query(Community).filter(Community.name.like(queryToSearch + "%")).all()

        # jsonReturn = {}
        # jsonReturn.communities = []

        # for tempCommunity in communityList:
        #     jsonReturn.communities.push(tempCommunity)

        return jsonify(communities = [i.serialize for i in communityList])
    else:
        flash("Arguments missting")
    
   




