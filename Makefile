default: server

env:
	pyvenv venv

install:
	pip install --upgrade pip
	pip install -r requirements.txt

installLin:
	sudo apt-get -y install postgresql
	sudo apt-get -y install python-psycopg2
	sudo apt-get -y install libpq-dev
	sudo apt-get -y build-dep python-psycopg2
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
	createuser -U postgres -h localhost -p 5432 -d -P amable # -createDB|-PromptPWD
	createdb -U amable -h localhost -p 5432 amable_development
	python db/manage.py version_control

version_control:
	python db/manage.py version_control