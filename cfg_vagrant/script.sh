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
sudo -i -u postgres
createuser -U postgres -D amable_development
createuser -U postgres -D amable
psql -U postgres -f /var/lib/pgsql/sql_script.sql

# PYTHON

# We need wget
sudo yum install -y wget


sudo yum -y update
sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python35u-3.5.2
sudo yum -y install python35u-pip
sudo yum -y install python35u-devel
sudo yum -y install postgresql-devel

cd /home/vagrant/sync

if [ ! -d "/home/vagrant/sync/venv" ]; then
	pyvenv-3.5 venv
fi

source venv/bin/activate
make install



# Lets grab Python 3.5.1
#cd /tmp
#wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz

# Install Python 3.5.1
#sudo yum install -y zlib-devel
#tar xzf Python-3.5.1.tgz
#cd Python-3.5.1
#./configure --prefix=/usr/local --with-zlib=/usr/include
#sudo make altinstall

# install pip
#cd /tmp
#wget https://bootstrap.pypa.io/get-pip.py
