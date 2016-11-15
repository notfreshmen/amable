import os
from flask import Blueprint, render_template, redirect, request, flash, jsonify, abort
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


@communities.route('/communities/create/process', methods=['POST'])
@login_required
def create_community():
    banner_url = "http://dsedutech.org/images/demo/placement_banner1.jpg"
    thumbnail_url = "http://i.imgur.com/7mo7QHW.gif"
    form = CommunityCreateForm(request.form)

    if form.validate():

        # First thing we are going to do is create a
        # Community object with the data from our form.
        newCommunity = Community(
            name=form.name.data,
            description=form.description.data,
            nsfw=form.nsfw.data
        )

        s.add(newCommunity)
        s.commit()  # we need to create a record so we have the id

        # Now we have a community with an ID. Lets create
        # a directory to upload image files to.
        community_upload_relative = '/communities/' + str(newCommunity.id)
        community_upload_url = './amable/uploads' + community_upload_relative

        if not os.path.exists(community_upload_url):
            os.makedirs(community_upload_url)

        # Lets do checks for Banner
        if 'banner' in request.files:
            banner_file = request.files['banner']

            if banner_file.filename != '':
                if allowed_file(banner_file.filename):
                    banner_filename = 'banner_' + \
                        secure_filename(banner_file.filename)

                    # Save | Upload Banner file
                    fullPath = os.path.join(
                        community_upload_url, banner_filename)

                    banner_file.save(fullPath)

                    banner_url = fullPath
                else:
                    flash('Banner filetype is not allowed, could not upload')
            else:
                flash('Banner file name cannot be empty')

        # Now lets do checks for Thumbnail
        if 'thumbnail' in request.files:
            thumbnail_file = request.files['thumbnail']

            if thumbnail_file.filename != '':
                if allowed_file(thumbnail_file.filename):
                    thumbnail_filename = 'thumbnail_' + \
                        secure_filename(thumbnail_file.filename)

                    # Save | Upload Thumbnail File
                    fullPath = os.path.join(
                        community_upload_url, thumbnail_filename)

                    thumbnail_file.save(fullPath)

                    thumbnail_url = fullPath
                else:
                    flash('Thumbnail filetype is not allowed, could not upload')
            else:
                flash('Banner file name cannot be empty')

        newCommunity.banner_url = banner_url
        newCommunity.thumbnail_url = thumbnail_url
        s.commit()
        return redirect('/communities/' + newCommunity.permalink)
