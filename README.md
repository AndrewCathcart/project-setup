# project-setup

## Description
This project is built using [Python3](https://www.python.org/download/releases/3.0/). 

It uses [Pipenv](https://docs.pipenv.org/en/latest/) for managing dependencies.

This script is for automating the initial steps usually completed when starting a new python project;
- create a project folder at the specified destination
- create a repo on Github
- add origin remote
- install autopep8 through pipenv
- create an empty README.md & .gitignore
- perform the initial commit of these files
- open the project in VSCode.

## Installation
`git clone "git@github.com:AndrewCathcart/project-setup.git"`

`cd project-setup`

`pipenv install` (or `pip install pipenv` followed by `pipenv install` if you don't already have pipenv)

Navigate to `setup-commands.sh` and make sure to change the `INSTALLATION_PATH` and `PROJECT_PATH` variables. 
- INSTALLATION_PATH is, intuitively, where you cloned the repository to.
- PROJECT_PATH is the desired location to store your new project folder in, e.g. `/Users/JoeBloggs/Projects/Python Projects/$1` making sure to keep the bash variable $1 at the end of the string

Create a secrets.py inside the project-setup folder.

Navigate to `create_project.py`
- Change the path variable to where you'd like your projects to live e.g. `path = /Users/JoeBloggs/Projects/Python Projects/`
create a secrets.py inside the project-setup folder

If you have Two Factor Authentication setup on your Github account you'll need to;
- Generate an access token for the desired account at https://github.com/settings/tokens 
- Store the above token in a string named PERSONAL_ACCESS_TOKEN inside secrets.py

If you do not have Two Factor Authentication setup;
- Simply add USERNAME and PASSWORD strings to a secrets.py containing your Github login information

Finally source or alias the bash script for ease of use;
- add `source /Users/andrew.cathcart/dev/python/project-setup/setup-commands.sh` to your .bashrc or .zshrc profile & reload the terminal

## Usage
`create_project <project_name>`

## To-do
- Add support for environment variables instead of a secrets.py
