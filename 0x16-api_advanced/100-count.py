#!/usr/bin/python3
"""Module for task 3"""

def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""

    import requests

    # Make the API request
    sub_info = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        params={"after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    # Check for errors in the API response
    if sub_info.status_code != 200:
        print("None")
        return None

    info = sub_info.json()

    # Extract titles from the API response
    hot_titles = [child.get("data").get("title") for child in info.get("data").get("children")]

    # Create a dictionary to store the count of each word
    if not word_count:
        word_count = {word: 0 for word in word_list}

    # Count occurrences of each word in the titles
    for title in hot_titles:
        words_in_title = title.lower().split()
        for word in word_list:
            word_count[word] += words_in_title.count(word.lower())

    # Check if there are more pages of results
    if not info.get("data").get("after"):
        # Sort and print the results
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        # Recursive call for the next page of results
        count_words(subreddit, word_list, word_count, info.get("data").get("after"))

if __name__ == "__main__":
    # Example usage
    subreddit_name = input("Enter the subreddit name: ")
    keywords = input("Enter keywords separated by spaces: ").split()
    count_words(subreddit_name, keywords)
