import sys
from os.path import abspath, join, dirname


root_path = abspath(join(dirname(__file__), '..'))


def pytest_sessionstart(session):
    sys.path.insert(0, root_path)
