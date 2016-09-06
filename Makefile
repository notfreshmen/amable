default: server

env:
	pyvenv venv

install:
	pip install -r requirements.txt

server:
	python run.py

test:
	nosetests

lint:
	pycodestyle .
