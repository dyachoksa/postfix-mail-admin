# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.box_version = "1.0.282"
  config.vm.hostname = "postfix-mail.local"

  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider "hyperv" do |h|
    h.cpus = 2
    h.maxmemory = 2048
    h.memory = 1024
    h.vmname = "Postfix Mail"
  end
end
