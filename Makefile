default: server

env:
	pyvenv venv

install:
	pip install -r requirements.txt

server:
	python run.py

test:
	nosetests --with-coverage --cover-package=psn --rednose

lint:
	pycodestyle . --show-source --show-pep8 --exclude=venv/* --ignore=E402
