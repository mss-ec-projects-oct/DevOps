#!/bin/bash
echo "please provide a username to create." 
read user
sudo useradd $user
sudo passwd $user
sudo sed -i "50i $user    ALL=(ALL:ALL) ALL" /etc/sudoers
sudo sed -i 62s/^/#/ /etc/ssh/sshd_config
sudo mkdir /home/$user
sudo chown $user:$user /home/$user
