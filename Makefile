default: server

env:
	pyvenv venv

install:
	pip install --upgrade pip
	pip install -r requirements.txt

console:
	PYTHONSTARTUP=./console.py python

server:
	python ./server.py

test:
	mamba --enable-coverage --format=documentation

lint:
	pycodestyle .

coverage:
	coverage report

db_setup:
	createuser -U postgres -h localhost -p 5432 psn
	createdb -h localhost -p 5432 psn_development
	python db/manage.py version_control
