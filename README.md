# Amable

[![CircleCI](https://img.shields.io/circleci/project/notfreshmen/amable.svg?maxAge=2592000?style=flat-square)](https://circleci.com/gh/notfreshmen/amable) [![Code Climate](https://img.shields.io/codeclimate/github/notfreshmen/amable.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/amable) [![Code Climate](https://img.shields.io/codeclimate/coverage/github/notfreshmen/amable.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/amable/coverage)

## Installation

### General

You'll need Python 3.5.1 installed. You can do this with [pyenv](https://github.com/yyuu/pyenv).

Then, you'll need to create the virtual environment with `pyvenv`, so run:

```
$ make env
```

Now activate the environment. This will depend on your system, but with Bash:

```
$ source venv/bin/activate
```

To install dependencies, run:

```
$ make install
```

To set up the database, you'll need [PostgreSQL](https://www.postgresql.org/) installed. To set up the development database, run:

```
$ make db_setup
```

### Assets

You'll need Node.js 6.5.0 installed. You can do this with [nvm](https://github.com/creationix/nvm).

Then, just install the dependencies with `npm`:

```
$ npm install
```

## Development

### Running everything

You can use Honcho to run everything in one foreground process:

```
$ honcho start
```

This will run the development server and watch assets for you.

### Running a development server

To start a development server, run:

```
$ make server
```

It will start on [http://localhost:5000](http://localhost:5000).

### Starting a console

To start a REPL with access to the application, run:

```
$ make console
```

This will give you access to the `amable` module.

### Database

#### Creating a new migration

To make a new migration, use the database script:

```
$ python db/manage.py script "add users table"
```

#### Running the migrations

To run the migrations:

```
$ python db/manage.py upgrade
```

#### Rollback migrations

To rollback the previous migration:

```
$ python db/manage.py downgrade
```

### Building assets

To just build the assets, run:

```
$ gulp build
```

To watch assets for changes, run:

```
$ gulp watch
```

### Running tests

We're using [mamba](https://github.com/nestorsalceda/mamba) for tests. To run all of the tests, run:

```
$ make test
```

### Linting

To run code linting, run:

```
$ make lint
```

### Coverage

To show test coverage, run:

```
$ make coverage
```
