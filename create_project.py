import sys
import os
from github import Github

# path of the project folder you'd like to create the project in.
path = "/Users/andrew.cathcart/dev/python/"


def create_project():
    ''' Creates a project folder at the specified path & sets up a repo on your Github account. '''
    # TODO error handling
    project_name = str(sys.argv[1])
    username = sys.argv[2]
    password = sys.argv[3]

    full_project_path = path + project_name
    user = Github(username, password)

    os.makedirs(full_project_path)
    repo = user.create_repo(project_name)

    print("Successfully created a project at", full_project_path)
    print("Successfully created a repository named",
          project_name, "for Github account", username)


if __name__ == "__main__":
    create_project()
