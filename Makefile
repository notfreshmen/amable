default: server

env:
	pyvenv venv

install:
	pip install -r requirements.txt

server:
	python run.py

test:
	nosetests --with-coverage --cover-package=app

lint:
	pycodestyle psn/
