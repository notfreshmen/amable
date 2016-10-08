# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
	config.vm.box = "centos/7"
	config.vm.synced_folder ".", "/home/vagrant/sync", type: "virtualbox"
	config.vm.provision "shell", path: "cfg_vagrant/script.sh"
end
