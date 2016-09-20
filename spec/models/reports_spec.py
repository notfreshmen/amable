from expects import *
from models.report import Report
from amable import session

with context('models'):
    with context('report'):
        with context('Report'):

            with context('__init__'):

                with it('create report'):
                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user_id=1,
                        category="misc"
                    )

                    expect(report.title).to(equal('Hey Pablo'))

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
                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user_id=1,
                        category="misc"
                    )

                    reportModTime = report.date_modified

                    s = session()
                    s.add(report)
                    s.commit()

                    expect(report.title).to(equal('Hey Pablo'))

                    # Change info
                    report.title = "Bye Pablo"
                    s.commit()

                    expect(report.title).to(equal('Bye Pablo'))
                    expect(report.date_modified).not_to(equal(reportModTime))

                    s.delete(user)

            with context('__repr__'):
                with it('returns the username'):
                    report = Report(
                        title="Hey Pablo",
                        content="Jokes!",
                        user_id=1,
                        category="misc"
                    )

                    expect(user.__repr__()).to(equal("<Report 'Hey Pablo'>"))
