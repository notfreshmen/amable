from sqlalchemy.ext.declarative import declarative_base


def update(self, data):
    for key in data:
        if data[key] == "":
            data[key] = None

        setattr(self, key, data[key])

    return self


Base = declarative_base()

Base.update = update
