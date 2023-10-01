#!/usr/bin/python3
"""Uses Github API to retrieve last 10 commits from a repo"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    # Fetch the API url
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            owner, repo_name)

    # Set limit for no of commits to fetch
    params = {'per_page': 10}

    # Make a GET request to API
    response = requests.get(url, params=params)

    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
