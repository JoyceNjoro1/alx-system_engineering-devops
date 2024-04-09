#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    else:
        return 0

# Test the function
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))

