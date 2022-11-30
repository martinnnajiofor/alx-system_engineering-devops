#!/usr/bin/python3
"""
 queries the Reddit API and returns a list containing the titles
 of all hot articles for a given subreddit.
 If no results are found for the given subreddit,
 the function should return None.
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of the titles of all hot posts listed for a subreddit"""
    headers = {"user-agent": "holberton"}
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    subdata = requests.get(url, headers=headers, params=params)

    if subdata.status_code != 200:
        return None
    data = json.loads(subdata.text).get('data').get('children')
    after = json.loads(subdata.text).get('data').get('after')
    if data is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for item in data:
            hot_list.append(item.get('data').get('title'))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
