from expects import *
from flask_sqlalchemy import SQLAlchemy

from psn import db


with context('models'):
    with context('db'):
        with it('is a SQLAlchemy instance'):
            expect(db).to(be_a(SQLAlchemy))
