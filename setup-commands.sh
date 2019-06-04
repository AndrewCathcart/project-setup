#!/bin/bash

function create_project() {
    INSTALLATION_PATH = "/Users/andrew.cathcart/dev/python/project-setup"
    cd "$INSTALLATION_PATH"

    pipenv run python3 create_project.py $1
    PROJECT_DIRECTORY="/Users/andrew.cathcart/dev/python/$1"
    if [ -d "$PROJECT_DIRECTORY" ]; then
        cd "$PROJECT_DIRECTORY"
        else
        echo "Invalid Directory"
        return 0
    fi

    git init
    git remote add origin git@github.com:AndrewCathcart/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}
