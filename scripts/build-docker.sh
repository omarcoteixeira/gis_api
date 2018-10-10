#!/usr/bin/env bash

apt update

# Add ubuntugis repository and update/upgrade packages
add-apt-repository -y ppa:ubuntugis/ppa
apt update
apt upgrade

# Install GDAL essential packages
apt install -y libgdal-dev libevent-dev python-dev build-essential
apt install -y libgdal1h libgdal-dev python-gdal

# Update python pip and setuptools
pip install -U  pip
pip install -U setuptools
pip install -U wheel

#pip install virtualenv
#
#rm -rf venv/
#
#cd server
#
#virtualenv venv
#/bin/bash -c "source venv/bin/activate"