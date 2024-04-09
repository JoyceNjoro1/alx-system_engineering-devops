#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}  # Reddit API requires a custom User-Agent
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

# Test the function
if __name__ == '__main__':
    subreddit = "programming"
    print(number_of_subscribers(subreddit))

    subreddit = "this_is_a_fake_subreddit"
    print(number_of_subscribers(subreddit))

