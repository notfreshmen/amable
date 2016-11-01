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
	AMABLE_ENV=test mamba --enable-coverage --format=documentation

lint:
	pycodestyle .

js_lint:
	standard ./amable/assets/jsc/**/*.js

coverage:
	coverage report

db_user_setup:
	createuser -U postgres -h localhost -p 5432 -d -w amable
	sudo -u postgres psql -U postgres -c "alter user amable with password 'domislove';"

dbsync:
	dropdb -U amable amable_development --if-exists
	createdb -U amable -O amable -h localhost -p 5432 amable_development
	python db/manage.py version_control
	python db/manage.py upgrade

	dropdb -U amable amable_test --if-exists
	createdb -U amable -O amable -h localhost -p 5432 amable_test
	AMABLE_ENV=test python db/manage.py version_control
	AMABLE_ENV=test python db/manage.py upgrade

version_control:
	python db/manage.py version_control

db_upgrade:
	python db/manage.py upgrade
	AMABLE_ENV=test python db/manage.py upgrade
erd:
	eralchemy -i postgres://amable:domislove@localhost:5432/amable_development -o docs/erd.pdf
