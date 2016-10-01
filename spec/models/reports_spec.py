from expects import *
from amable.models.report import Report
from amable.models.user import User
from amable import session

s = session()

with context('amable.models'):
    with context('report'):
        with context('Report'):

            with context('__init__'):

                with it('create report'):
                    s = session()

                    user = User(
                        username="pablo",
                        email="pablo@pablo.com",
                        password="pablo",
                        name="Pablo",
                        bio="Pablo",
                        website="reev.us",
                        location="pablo",
                        phone="4018888888",
                        dob="1999-01-08")

                    s.add(user)
                    s.commit()

                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user_id=user.id,
                        category="misc"
                    )
                    s.add(report)
                    s.commit()

                    expect(report.title).to(equal('Hey Pablo'))
                    expect(report.user_id).to(equal(user.id))

                    # User.query.filter(User.id==user.id).delete()
                    # Report.query.filter(Report.id==eport.id).delete()
                    s.delete(report)
                    s.delete(user)
                    s.commit()

                with it('edit report'):
                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user_id=1,
                        category="misc"
                    )

                    expect(report.title).to(equal('Hey Pablo'))
                    expect(report.content).to(equal('Jokes!'))

                    # Change info
                    report.title = "Bye Pablo"
                    report.content = "Statements!"

                    expect(report.title).to(equal('Bye Pablo'))
                    expect(report.content).to(equal('Statements!'))

                with it('changes attributes and date'):
                    s = session()

                    user = User(
                        username="pablo",
                        email="pablo@pablo.com",
                        password="pablo",
                        name="Pablo",
                        bio="Pablo",
                        website="reev.us",
                        location="pablo",
                        phone="4018888888",
                        dob="1999-01-08")

                    s.add(user)
                    s.commit()

                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user_id=user.id,
                        category="misc"
                    )
                    s.add(report)
                    s.commit()

                    reportModTime = report.date_modified


                    expect(report.title).to(equal('Hey Pablo'))

                    # Change info
                    report.title = "Bye Pablo"
                    s.commit()

                    expect(report.title).to(equal('Bye Pablo'))
                    expect(report.date_modified).not_to(equal(reportModTime))

                    s.delete(report)
                    s.delete(user)
                    s.commit()

            with context('__repr__'):
                with it('returns the report'):
                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user_id=1,
                        category="misc"
                    )

                    expect(report.__repr__()).to(equal("<Report 'Hey Pablo'>"))
