function step1 {
    yum install -y  bash-completion.noarch vim
    dnf install -y iproute-tc
}

function step2 {
    echo "Disable Swap and Set SELinux in permissive mode"
    swapoff -a
    sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
    setenforce 0
    sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
}



function step3master {
    echo "Configure Firewall Rules on Master Nodes"
    firewall-cmd --permanent --add-port=6443/tcp
    firewall-cmd --permanent --add-port=2379-2380/tcp
    firewall-cmd --permanent --add-port=10250/tcp
    firewall-cmd --permanent --add-port=10251/tcp
    firewall-cmd --permanent --add-port=10252/tcp
    firewall-cmd --reload
    modprobe br_netfilter
    sh -c "echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables"
    sh -c "echo '1' > /proc/sys/net/ipv4/ip_forward"
}

function step3slave {
    echo "Configure Firewall Rules on Worker Nodes"
    firewall-cmd --permanent --add-port=10250/tcp
    firewall-cmd --permanent --add-port=30000-32767/tcp                                                  
    firewall-cmd --reload
    modprobe br_netfilter
    sh -c "echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables"
    sh -c "echo '1' > /proc/sys/net/ipv4/ip_forward"
}

function step4 {
    echo "Install CRI-O on Master and Worker Nodes"
    # Create the .conf file to load the modules at bootup

cat <<EOF | sudo tee /etc/modules-load.d/crio.conf
overlay
br_netfilter
EOF

    sudo modprobe overlay
    sudo modprobe br_netfilter

# Set up required sysctl params, these persist across reboots.
cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

sudo sysctl --system


OS=CentOS_8
VERSION=1.20:1.20.0
sudo curl -L -o /etc/yum.repos.d/devel:kubic:libcontainers:stable.repo https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/devel:kubic:libcontainers:stable.repo
sudo curl -L -o /etc/yum.repos.d/devel:kubic:libcontainers:stable:cri-o:$VERSION.repo https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable:cri-o:$VERSION/$OS/devel:kubic:libcontainers:stable:cri-o:$VERSION.repo
sudo yum install cri-o cri-tools
sudo systemctl daemon-reload
sudo systemctl enable crio --now

cat <<EOF | sudo tee /etc/crio/crio.conf.d/02-cgroup-manager.conf
[crio.runtime]
conmon_cgroup = "pod"
cgroup_manager = "cgroupfs"
EOF

}

function step5 {
    echo "Install kubelet, Kubeadm and kubectl"
    cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
    [kubernetes]
    name=Kubernetes
    baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
    enabled=1
    gpgcheck=1
    repo_gpgcheck=1
    gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
    exclude=kubelet kubeadm kubectl
EOF

    dnf install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
    systemctl enable --now kubelet

}



echo "ready to exec kubeadm -init"
