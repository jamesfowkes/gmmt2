#!/bin/bash

export WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source `locate /virtualenvwrapper.sh`

workon gmmt2

python3 runapp.py $1 $2 $3 $4
