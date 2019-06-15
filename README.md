# project-setup

## Description
This project is built using [Python3](https://www.python.org/download/releases/3.0/). 

It uses [Pipenv](https://docs.pipenv.org/en/latest/) for managing dependencies.

It creates a project folder at the specified destination, creates a git repository with the project name, sets the upstream, installs autopep8 through pipenv, commits a README.md, Pipfile & Pipefile.lock before finally opens the project in VSCode.

## Installation
`git clone "git@github.com:AndrewCathcart/project-setup.git"`

`cd project-setup`

`pipenv install` (or `pip install pipenv` followed by `pipenv install` if you don't already have pipenv)

navigate to `setup-commands.sh` and make sure to change the `INSTALLATION_PATH` and `PROJECT_PATH` variables. 
- INSTALLATION_PATH is, intuitively, where you cloned the repository to.
- PROJECT_PATH is the desired location to store your new project folder in, e.g. `/Users/JoeBloggs/Projects/Python Projects/$1` making sure to keep the bash variable $1 at the end of the string

Source the bash script for ease of use, e.g. add `source /Users/andrew.cathcart/dev/python/project-setup/setup-commands.sh` to your .bashrc or .zshrc profile & reload the terminal

If you have Two Factor Authentication setup on your Github account you'll need to;
- generate an access token for the desired account at https://github.com/settings/tokens 
- create a secrets.py inside the project-setup folder and store the above token in a string named PERSONAL_ACCESS_TOKEN

Otherwise simply alter the username & password string inside create_project.py

## Usage
`create_project <project_name>`
