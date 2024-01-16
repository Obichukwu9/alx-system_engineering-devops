#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])

            if not data:
                print('None')
            else:
                for child in data:
                    print(child.get("data").get("title"))
        else:
            print('None')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print('None')

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name)]
