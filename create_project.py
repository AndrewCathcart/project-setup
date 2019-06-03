import sys
import os
from github import Github
from secrets import PERSONAL_ACCESS_TOKEN

# path of the project folder you'd like to create the project in.
path = "/Users/andrew.cathcart/dev/python/"

# specify username & pass3ord or use personal access token generated at https://github.com/settings/tokens
username = ""
password = ""
token = ""  # PERSONAL_ACCESS_TOKEN


def create_project():
    ''' Creates a project folder at the specified path & sets up a repo on your Github account. '''
    project_name = str(sys.argv[1])
    full_project_path = path + project_name

    if token:
        g = Github(token)
    elif username and password:
        g = Github(username, password)
    else:
        print("Please specify either an access token or username and password in create_project.py")
        return 0

    os.makedirs(full_project_path)
    repo = g.get_user().create_repo(project_name)

    print("Successfully created a project at", full_project_path)
    print("Successfully created a repository named", project_name)


if __name__ == "__main__":
    create_project()
