# Update the packages first
sudo yum update -y

# Install PostgreSQL
sudo yum install -y postgresql-server postgresql-contrib
sudo postgresql-setup initdb
sudo rm /var/lib/pgsql/data/pg_hba.conf
sudo cp /home/vagrant/sync/cfg_vagrant/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
sudo chown postgres /var/lib/pgsql/data/pg_hba.conf
sudo chmod 600 /var/lib/pgsql/data/pg_hba.conf
sudo systemctl start postgresql
sudo systemctl enable postgresql
createuser -U postgres -h localhost -p 5432 -d -w amable
sudo -u postgres psql -U postgres -c "alter user amable with password 'domislove';"
echo '=> Postgres installed and configured'

# Install Python
sudo yum -y install wget git curl install yum-utils zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel python35u-devel graphviz-devel postgresql-devel postgresql-libs python-devel

git clone https://github.com/yyuu/pyenv.git /home/vagrant/.pyenv

sudo chmod 777 -R /home/vagrant/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /home/vagrant/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_profile

source /home/vagrant/.bash_profile

pyenv install 3.5.1

cd /home/vagrant/sync

if [ ! -d "/home/vagrant/sync/venv" ]; then
	pyvenv-3.5 venv
fi

source venv/bin/activate

sudo easy_install pip

make install

make db_user_setup
make db_setup

echo '=> Python installed and configured'

# Node
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash
source /home/vagrant/.bash_profile
nvm install v6.5.0
nvm use v6.5.0
nvm alias default v6.5.0
curl -o- -L https://yarnpkg.com/install.sh | bash

echo 'export PATH="$HOME/.yarn/bin:$PATH"' >> /home/vagrant/.bash_profile

source /home/vagrant/.bash_profile

yarn

echo '=> Node.js installed and configured'
