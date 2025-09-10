#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose -y
git clone https://github.com/Digzopian-Tendencies/Digzopian-Stakz.git
cd Digzopian-Stakz
docker-compose up -d --build
