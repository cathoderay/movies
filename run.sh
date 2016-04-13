#!/bin/bash

myecho() {
    echo -e "\e[0;32m* $1\e[0m"
}

# Quickstart
myecho "Cloning repository..."
git clone https://github.com/cathoderay/movies.git

myecho "Entering repository..."
cd movies

myecho "Starting a virtualenv..."
virtualenv .env

myecho "Activating the virtualenv..."
source .env/bin/activate

myecho "Installing pip requirements..."
pip install -r requirements.txt

cd website

myecho "Everything seems to be great. Running server."
python manage.py runserver 0.0.0.0:8000


