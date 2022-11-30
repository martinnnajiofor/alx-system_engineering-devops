#!/usr/bin/python3
import re
import requests
headers = {'user-agent': 'Reddit Scraper'}

def recurse(subreddit, hot_list=[], after=None, count=None):
    """Recurses and returns a list containing the titles
    of all hot articles for a given subreddit"""
    if after is None and count is None:
        after = ''
        count = 0

    hot_endpoint = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'

    url = hot_endpoint.format(subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        hot = response.json()
        children = hot.get("data").get("children")
        after = hot.get("data").get("after")
        for child in children:
            title = child.get("data").get("title")
            hot_list.append(title)
        if len(hot_list) < 1:
            return None
        while True:
            if after is not None:
                recurse(subreddit, hot_list, after, count)
                break
            if after is None:
                break
        return hot_list
    if response.status_code == 404 or response.status_code == 302:
        return None



def counter():
    """generator increasing by one"""
    c = 0
    while True:
        yield c
        c += 1


def count_words(subreddit, word_list):
    result = recurse(subreddit)
    if result is None:
        print()
    elif result is not None:
        word_dict = {}

        for text in result:
            for word in word_list:
                if word not in word_dict.keys():
                    word_dict[word] = 0
                # create regex
                regex = re.compile(r"\b" + word + r"\b", re.I)
                # check regex results
                word_dict[word] += len(regex.findall(text))

        s = sorted(list(word_dict.values()))
        s.reverse()
        reversed_dict = {}
        counting = counter()
        for k, v in word_dict.items():
            reversed_dict[f"{v}.{next(counting)}"] = k
        final = []
        for each in s:
            for j in reversed_dict.keys():
                if str(each) in j:
                    if f"{reversed_dict[j]}: {j.split('.')[0]}" not in final:
                        final.append(f"{reversed_dict[j]}: {j.split('.')[0]}")

        for each in final:
            if ": 0" not in each:
                print(each)
