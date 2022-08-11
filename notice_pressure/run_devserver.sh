#!/bin/bash

service mysql start
export FLASK_APP=notice_pressure/app
export FLASK_ENV=dev
flask run