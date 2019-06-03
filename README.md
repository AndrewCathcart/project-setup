# Development
This project is built using [Python3](https://www.python.org/download/releases/3.0/). 

It uses [Pipenv](https://docs.pipenv.org/en/latest/) for managing dependencies.

# Installation
`git clone "git@github.com:AndrewCathcart/project-setup.git"`

`cd project-setup`

`pipenv install` (or `pip install pipenv` followed by `pipenv install`)

navigate to `setup-commands.sh` and make sure to alter the location of your workspace (change `cd /Users/andrew.cathcart/dev/python/$1` to e.g. `cd /Users/JoeBloggs/Projects/Python Projects/$1`)

Source the bash script for ease of use, e.g. add `source /Users/andrew.cathcart/dev/python/project-setup/setup-commands.sh` to your .bashrc or .zshrc profile & reload the terminal

If you have Two Factor Authentication setup on your Github account you'll need to;
- generate an access token at https://github.com/settings/tokens 
- create a secrets.py inside the project-setup folder and store the above token in a string named PERSONAL_ACCESS_TOKEN

Otherwise simply alter the username & password string inside create_project.py

# Usage
`create_project <project_name>`
