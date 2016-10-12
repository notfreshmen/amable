from expects import *

from amable import session
from amable.models.hashtag import Hashtag, update_date_modified

from spec.factories.hashtag_factory import HashtagFactory


s = session()

with context('amable.models'):
    with before.each:
        self.hashtag = HashtagFactory.create()

    with after.all:
        s.query(Hashtag).delete()
        s.commit()

    with context('hashtag'):
        with context('Hashtag'):
            with context('__init__'):
                with it('create'):
                    hashtag = Hashtag(
                        tag='reevus'
                    )

                    expect(hashtag.tag).to(equal('reevus'))

            with context('__repr__()'):
                with it('returns the id of the hashtag'):
                    expect(self.hashtag.__repr__()).to(contain("<Hashtag 'reevus'>"))

        with context('update_date_modified'):
            with it('updates the date for the hashtag'):
                date_modified = self.hashtag.date_modified

                update_date_modified(Hashtag, session, self.hashtag)

                expect(self.hashtag.date_modified).not_to(equal(date_modified))
