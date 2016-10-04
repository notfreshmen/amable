import factory

from amable import session

from amable.models.report import Report

from spec.factories.user_factory import UserFactory


class ReportFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Report
        sqlalchemy_session = session

    title = "Hey Pablo"
    content = "Jokes!"
    user = factory.SubFactory(UserFactory)
    category = "misc"
