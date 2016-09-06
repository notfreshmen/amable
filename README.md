# Prayer Social Network (PSN)

[![CircleCI](https://img.shields.io/circleci/project/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://circleci.com/gh/notfreshmen/psn) [![Code Climate](https://img.shields.io/codeclimate/github/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/psn) [![Code Climate](https://img.shields.io/codeclimate/coverage/github/notfreshmen/psn.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/psn/coverage)

## Installation

You'll need Python 3.5.1 installed. Then, create the virtual environment with `pyvenv`:

```
$ pyvenv venv
```

Then install the dependencies:

```
$ pip install -r requirements.txt
```

## Development

### Running a development server

```
$ python run.py
```

A server will start on [http://localhost:5000](http://localhost:5000).

### Running tests

We're using `nose` for tests. To run all of the tests, just use:

```
$ nosetests
```
