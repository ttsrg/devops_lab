#!/usr/bin/python

import sys
import requests
import getpass

if __name__ == "__main__":

    try:

        if str(sys.argv[1]) == "-h":
            print("Usage: ./pr-stats.py [yours gitloginname] [repo's URL address]")
            exit()

        if str(sys.argv[1]) == "--help":
            print("Usage: ./pr-stats.py [yours gitloginname] [repo's URL address]")
            exit()

        if str(sys.argv[1]) == "--version":
            print("pr-stats.py Ver. 1.0")
            exit()

        if len(sys.argv) < 3:
            print("Try `python pr-stats.py -h` or `python pr-stats.py --help`")
            exit()

    except IndexError:
        print("!!! Exception !!! No one options was entered.")
        print("Try `python pr-stats.py -h` or `python pr-stats.py --help`")
        exit()

gitloginname = sys.argv[1]
gitrepoapi = sys.argv[2]
gitpasswd = getpass.getpass(
    prompt='Please, enter your GIThub password: ', stream=None)

# gitloginname = 'ttsrg'
# gitrepoapi = "https://api.github.com/repos/alenaPy/devops_lab/pulls"

reqgit = requests.get(gitrepoapi, auth=(gitloginname, gitpasswd)).json()

for i in range(30):
    print("Title: %s" % reqgit[i]['title'])
    print("Owner: %s" % reqgit[i]['head']['repo']['owner']['login'])
    print("State: %s" % reqgit[i]['state'])
    print("Created_at: %s" % reqgit[i]['head']['repo']['created_at'])
    print("Pushed_at: %s" % reqgit[i]['head']['repo']['pushed_at'])
    print("Updated_at: %s" % reqgit[i]['head']['repo']['updated_at'])
    print("Closed_at: %s" % reqgit[i]['closed_at'])
    print("Size: %s" % reqgit[i]['head']['repo']['size'] + "\n---===---")
