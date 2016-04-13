#!/bin/bash

# Quickstart
git clone https://github.com/cathoderay/movies.git
cd movies
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
cd website
python manage.py runserver

