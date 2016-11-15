# Amable

[![CircleCI](https://img.shields.io/circleci/project/notfreshmen/amable.svg?maxAge=2592000?style=flat-square)](https://circleci.com/gh/notfreshmen/amable) [![Code Climate](https://img.shields.io/codeclimate/github/notfreshmen/amable.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/amable) [![Code Climate](https://img.shields.io/codeclimate/coverage/github/notfreshmen/amable.svg?maxAge=2592000?style=flat-square)](https://codeclimate.com/github/notfreshmen/amable/coverage)

## Memcache Setup
This was done on an Ubuntu machine. If you are on Windows/Macosx there is a brew setup for memcache. Here are some troubleshooting I went through for Ubuntu.

### Ubuntu/Centos

1. Install Memcache
  * https://www.digitalocean.com/community/tutorials/how-to-install-and-use-memcache-on-ubuntu-14-04
  * https://www.liquidweb.com/kb/how-to-install-memcached-on-centos-7/
2. Install Libraries if needed
  * If you get an error looking like this : 

```
Command "/home/benderm/Github/amable/venv/bin/python3.5 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-00gqva6p/pylibmc/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-huj0ozjx-record/install-record.txt --single-version-externally-managed --compile --install-headers /home/benderm/Github/amable/venv/include/site/python3.5/pylibmc" failed with error code 1 in /tmp/pip-build-00gqva6p/pylibmc/
```

Try running : 

```
$ sudo apt-get install libmemcached-dev zlib1g-dev
```

## Installation

You'll need [Vagrant](https://www.vagrantup.com) and [VirtualBox](https://www.virtualbox.org/) installed on your machine. Then, with a command line (Terminal on macOS and Linux, PowerShell or Command Prompt on Windows), you'll need to install the [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest) Vagrant plugin:

```
$ vagrant plugin install vagrant-vbguest
```

Then you can switch directories to wherever you have Amable and run:

```
$ vagrant up
```

This will boot the virtual machine. In order to install everything for Amable, SSH into it:

```
$ vagrant ssh
```

Then run the script and restart your session.

```
$ sh /home/vagrant/sync/cfg_vagrant/script.sh
$ exec $SHELL -l
```

### Troubleshooting

#### VirtualBox Guest Additions don't work on macOS

If you get an error something like this:

```
Failed to mount folders in Linux guest. This is usually because
the "vboxsf" file system is not available. Please verify that
the guest additions are properly installed in the guest and
can work properly. The command attempted was:

mount -t vboxsf -o uid=`id -u vagrant`,gid=`getent group vagrant | cut -d: -f3` home_vagrant_sync /home/vagrant/sync
mount -t vboxsf -o uid=`id -u vagrant`,gid=`id -g vagrant` home_vagrant_sync /home/vagrant/sync

The error output from the last command was:

/sbin/mount.vboxsf: mounting failed with the error: No such device
```

VirtualBox Guest Additions aren't working properly. Log into the box:

```
$ vagrant ssh
```

And then run:

```
$ sudo yum install -y kernel.x86_64 0:3.10.0-327.36.1.el7 kernel-devel
$ sudo ln -s /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions
$ exit
```

Now reload the box and SSH in again:

```
$ vagrant reload
$ vagrant ssh
```

Then run the installation script:

```
$ sh /home/vagrant/sync/cfg_vagrant/script.sh
$ exec $SHELL -l
```

## Development

To start any development, first start the Vagrant box, SSH into it, and change to the Amable directory.:

```
$ vagrant up
$ vagrant ssh
$ cd sync/
```

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

#### JavaScript Linting

To lint our JavaScript, you'll need to do the optional part above. Then run:

```
$ make js_lint
```

### Coverage

To show test coverage, run:

```
$ make coverage
```
### ER Diagrams

To make a new ER diagram:

```
$ make erd
```

This will output to `docs/erd.pdf`.
