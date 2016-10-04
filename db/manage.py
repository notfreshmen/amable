#!/usr/bin/env python

import sys
import os

from migrate.versioning.shell import main


# Changing the directory and importing is hacky!
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../')


from amable import app

if __name__ == '__main__':
    main(url=app.config['SQLALCHEMY_DATABASE_URI'],
         debug='False', repository='db')
