
moderators = Blueprint('moderators', __name__,
                        template_folder='../mods')

s = session()

@moderators.route('/moderators')
def index():


    return render_template('moderators/index.html',
                           title="Moderators",
                           moderators=moderators,
                           form=CommunitySearchForm())
