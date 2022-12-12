#!/bin/bash


virtualenv ~/.venv
echo 'source ~/.venv/bin/activate' >> ~/.bashrc
make install
curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'
unzip awscliv2.zip
sudo ./aws/install
rm -r aws
rm awscliv2.zip
make install
wget -O pgfutter https://github.com/lukasmartinelli/pgfutter/releases/download/v1.2/pgfutter_linux_amd64
chmod +x pgfutter
mv pgfutter 00_Source_Data/pgfutter

exit 1