from sqlalchemy import create_engine
from amable import app

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
