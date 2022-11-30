#!/usr/bin/python3
import requests
headers = {'user-agent': 'Reddit Scraper'}


def top_ten(subreddit):
    """Returns top ten hot results for a subreddit"""
    hot_endpoint = 'https://www.reddit.com/r/{}/hot.json?limit=10'
    url = hot_endpoint.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        hot = response.json()
        top10 = hot.get("data").get("children")
        for result in top10:
            print(result.get("data").get("title"))
    if response.status_code == 404 or response.status_code == 302:
        print(None)
