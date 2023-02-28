#!/bin/sh
export PATH=/usr/local/bin:$PATH;
yum update
yum install docker -y
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo docker pull ymsimsek/backend_flask:v1
sudo docker run --rm -p 4567:4567 -e FRONTEND_URL='*' -e BACKEND_URL='*' -d ymsimsek/backend_flask:v1