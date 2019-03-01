#!/usr/bin/python


import requests
import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('username')
parser.add_argument('url', help="URL")
parser.add_argument('--title', '-t', action="store_true", help="Show title")
parser.add_argument('--state', '-s', action="store_true", help="State of PR")
parser.add_argument('--created_at', '-c', action="store_true")
parser.add_argument('--updated_at', '-u', action="store_true")
parser.add_argument('--ownerurl', '-o', action="store_true", help="Owner URL")
parser.add_argument('--repo', '-r', action="store_true", help="Repo name")
parser.add_argument('--pushed_at', '-p', action="store_true")
args = parser.parse_args()
gitpasswd = getpass.getpass()
gitloginname = args.username
gitrepoapi = args.url


def repo_info(uname, pwd):
    reqgit = requests.get(gitrepoapi, auth=(gitloginname, gitpasswd)).json()

    if args.title:
        print("Title: %s " % str(reqgit['title']))
    if args.state:
        print("State: %s " % reqgit['state'])
    if args.created_at:
        print("Creation time: %s " % str(reqgit['created_at']))
    if args.updated_at:
        print("Updation time: %s " % str(reqgit['updated_at']))
    if args.ownerurl:
        print("Owner URL: %s " % (
            str(reqgit['base']['repo']['owner']['html_url'])))
    if args.repo:
        print("Repo name: %s " % reqgit['head']['repo']['name'])
    if args.pushed_at:
        print("Pushed_at: %s" % reqgit['head']['repo']['pushed_at'])


if __name__ == '__main__':
    repo_info(gitloginname, gitpasswd)
