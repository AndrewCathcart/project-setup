#!/bin/bash

function create_project() {
    cd
    pipenv run python3 create_project.py $1 $2 $3
    cd /Users/andrew.cathcart/dev/python/
    git init
    git remote add origin git@github.com:$2/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}
