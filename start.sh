#!/bin/bash

source .env

virtualenv python
python/bin/pip install -r requirements.txt
python/bin/python geoconnect/connect_database.py -h
