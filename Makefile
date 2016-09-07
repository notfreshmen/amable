default: server

env:
	pyvenv venv

install:
	pip install -r requirements.txt

console:
	PYTHONSTARTUP=./console.py python

server:
	python ./server.py

test:
	nosetests

lint:
	pycodestyle .
