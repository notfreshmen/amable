# Prayer Social Network (PSN)

[![CircleCI](https://img.shields.io/circleci/project/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://circleci.com/gh/notfreshmen/psn) [![Code Climate](https://img.shields.io/codeclimate/github/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/psn) [![Code Climate](https://img.shields.io/codeclimate/coverage/github/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/psn/coverage)

## Installation

You'll need Python 3.5.1 and installed. You can do this with [pyenv](https://github.com/yyuu/pyenv).

Then, you'll need to create the virtual environment with `pyvenv`, so run:

```
$ make env
```

To install dependencies, run:

```
$ make install
```

Now, you should have everything you need installed.

## Development

### Running a development server

To start a development server, run:

```
$ make server
```

It will start on [http://localhost:5000](http://localhost:5000).

### Running tests

We're using [nose](http://nose.readthedocs.io/en/latest/) for tests. To run all of the tests, run:

```
$ make test
```
