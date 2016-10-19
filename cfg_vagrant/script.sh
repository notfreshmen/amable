# Update
sudo yum update -y

# Postgres
sudo yum install -y postgresql-server postgresql-contrib
sudo postgresql-setup initdb
echo 'Postgres Installed'

# Postgres Config
sudo rm /var/lib/pgsql/data/pg_hba.conf
sudo cp /home/vagrant/sync/cfg_vagrant/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
sudo chown postgres /var/lib/pgsql/data/pg_hba.conf
sudo chmod 600 /var/lib/pgsql/data/pg_hba.conf
echo 'Postgres General Configuration Done'

# Set up Postgres Database Config
sudo cp /home/vagrant/sync/cfg_vagrant/sql_script.sql /var/lib/pgsql
sudo chown postgres /var/lib/pgsql/sql_script.sql
echo 'Postgres Database Configuration Done'

# Start Postgres and Enable
sudo systemctl start postgresql
sudo systemctl enable postgresql
echo 'Enabled Postgres'

# Create new Postgres user create db
#sudo -i -u postgres
createuser -U postgres -D amable
psql -U postgres -f /var/lib/pgsql/sql_script.sql

# PYTHON

# We need wget and git
sudo yum install -y wget git


sudo yum -y update
sudo yum -y install yum-utils
sudo yum -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel python35u-devel

git clone https://github.com/yyuu/pyenv.git /home/vagrant/.pyenv

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

sudo -u postgres psql -U postgres -c "alter user amable with password 'domislove';"

python db/manage.py version_control
python db/manage.py upgrade

AMABLE_ENV=test python db/manage.py version_control
AMABLE_ENV=test python db/manage.py upgrade

# Node
cd /tmp
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash
source /home/vagrant/.bash_profile
nvm install v6.5.0
nvm use v6.5.0
nvm alias default v6.5.0
curl -o- -L https://yarnpkg.com/install.sh | bash
yarn
