# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX_BASE = "debian/contrib-buster64"

$script_celery = <<-SCRIPT
apt update
apt-get install -y python3-pip
pip3 install celery
pip3 install -U "celery[redis]"
SCRIPT


$script_backend = <<-SCRIPT
apt update
apt-get install -y ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io

docker run -d --hostname my-rabbitmq  --network host --name celery-rabbitmq rabbitmq:3-management
docker run -d --network host --name celery-redis redis

apt-get install -y python3-pip
pip3 install celery flower
celery --broker=amqp://guest:guest@localhost:5672// --result-backend redis://localhost:6379/0 flower
SCRIPT

Vagrant.configure("2") do |config|
  config.vbguest.auto_update = false
  
  config.vm.define "worker1" do |worker1|
    worker1.vm.box = BOX_BASE
    worker1.vm.hostname = "worker1"
    worker1.vm.provision "shell", inline: $script_celery
    worker1.vm.network "private_network", ip: "192.168.56.11", virtualbox__intnet: true
    worker1.vbguest.auto_update = false
    worker1.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  end
  
  config.vm.define "worker2" do |worker2|
    worker2.vm.box = BOX_BASE
    worker2.vm.hostname = "worker2"
    worker2.vm.provision "shell", inline: $script_celery
    worker2.vm.network "private_network", ip: "192.168.56.12", virtualbox__intnet: true
    worker2.vbguest.auto_update = false
    worker2.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  end

  config.vm.define "loader" do |loader|
    loader.vm.box = BOX_BASE
    loader.vm.hostname = "loader"
    loader.vm.provision "shell", inline: $script_celery
    loader.vm.network "private_network", ip: "192.168.56.13", virtualbox__intnet: true
    loader.vbguest.auto_update = false
    loader.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  end

  config.vm.define "backend" do |backend|
    backend.vm.box = BOX_BASE
    backend.vm.hostname = "backend"
    #backend.memory = 1024  
    #backend.cpus = 2
    backend.vm.provision "shell", inline: $script_backend
    backend.vm.network "private_network", ip: "192.168.56.10", virtualbox__intnet: true
    backend.vm.network "forwarded_port", guest: 15672 , host: 15672
    backend.vm.network "forwarded_port", guest: 6379 , host: 6379
    backend.vm.network "forwarded_port", guest: 5555 , host: 5555
  end

end


