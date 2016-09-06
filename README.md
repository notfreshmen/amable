# Prayer Social Network (PSN)

[![CircleCI](https://img.shields.io/circleci/project/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://circleci.com/gh/notfreshmen/psn) [![Code Climate](https://img.shields.io/codeclimate/github/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/psn) [![Code Climate](https://img.shields.io/codeclimate/coverage/github/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/psn/coverage)

## Installation

### Web Server

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

We're using [nose](http://nose.readthedocs.io/en/latest/) for tests. To run all of the tests, run:

```
$ make test
```
