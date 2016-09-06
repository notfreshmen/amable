import sys,os

import nose

basedir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, basedir + '/../')

from app import psn
