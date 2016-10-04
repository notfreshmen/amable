from expects import *

from amable import session
from amable.models.report import Report, update_date_modified
from amable.models.user import User

from spec.factories.report_factory import ReportFactory
from spec.factories.user_factory import UserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.report = ReportFactory.create()

    with after.all:
        s.query(Report).delete()
        s.query(User).delete()
        s.commit()

    with context('report'):
        with context('Report'):
            with context('__init__'):
                with it('create'):
                    user = UserFactory.create()

                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user=user,
                        category="misc"
                    )

                    expect(report.title).to(equal('Hey Pablo'))
                    expect(report.user_id).to(equal(user.id))

            with context('__repr__()'):
                with it('returns the title of the report'):
                    expect(self.report.__repr__()).to(equal("<Report 'Hey Pablo'>"))

        with context('update_date_modified'):
            with it('updates the date for the report'):
                date_modified = self.report.date_modified

                update_date_modified(Report, session, self.report)

                expect(self.report.date_modified).not_to(equal(date_modified))
