import os
from flask import Blueprint, render_template, request, flash, jsonify, abort
from flask_login import login_required

from sqlalchemy import func
from sqlalchemy.orm import joinedload

from amable import session, app

from amable.models.community import Community
from amable.models.post import Post

from amable.forms.community_search_form import CommunitySearchForm
from amable.forms.community_create_form import CommunityCreateForm
from amable.forms.file_upload_test_form import FileTestForm

from amable.utils.files import allowed_file

from werkzeug.utils import secure_filename


communities = Blueprint('communities', __name__,
                        template_folder='../templates')

s = session()


@communities.route('/communities')
@login_required
def index():
    communities = s.query(Community).all()

    print(communities)

    return render_template('communities/index.html',
                           title="Communities",
                           communities=communities,
                           form=CommunitySearchForm())


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


@communities.route('/communities/create', methods=['GET'])
@login_required
def create():
    return render_template('communities/create.html',
                           form=CommunityCreateForm())


@communities.route('/communities/test', methods=['GET'])
@login_required
def test():
    return render_template('communities/test.html',
                           form=FileTestForm())


@communities.route('/communities/test/upload', methods=['POST'])
@login_required
def testupload():
    form = FileTestForm(request.form)

    if form.validate():

        if 'file_field' in request.files:
            file = request.files['file_field']

            if file.filename == '':
                return 'no filename'
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print(app.config['UPLOAD_FOLDER'])
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return filename
            else:
                return 'nah'
        else:
            return 'na'


# @communities.route('/communities/create/process', methods=['POST'])
# @login_required
# def create_community():
#     banner_url = ""
#     thumbnail_url = ""
#     form = CommunityCreateForm(request.form)

#     if form.validate():

#         # First lets upload the files

#         # Banner First
#         if 'banner' in request.files:
#             banner_file = request.files['banner']

#             if banner_file.filename == '':
#                 flash("No Selected Files")
#                 return redirect(url_for('.create'))
#             elif allowed_file(banner_file.filename):
#                 banner_filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 return redirect(url_for('.search'))
