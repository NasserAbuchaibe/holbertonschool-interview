#!/usr/bin/python3
"""sumary_line"""

import requests


def parse_hotart(hot_subreddits_list, word_list):
    """This method parses the hot articles"""
    dict_list = {}

    if hot_subreddits_list is None:
        return

    low_words = list(map(lambda x: x.lower(), word_list))

    for word in low_words:
        total = 0
        for hot_subreddit in hot_subreddits_list:
            if word in hot_subreddit.lower():
                total += hot_subreddit.lower().split().count(word)
        if total > 0:
            if word not in dict_list:
                dict_list[word] = total
            else:
                dict_list[word] += total

    result = sorted(dict_list.items(), key=lambda x: x[0])
    result = sorted(result, key=lambda x: x[1], reverse=True)
    for key, value in result:
        print("{}: {}".format(key, value))


def count_words(subreddit, word_list, hot_list=[], after=""):
    """This method counts the words"""
    headers = {"user-agent": "NasserDev17"}

    if after is None:
        return parse_hotart(hot_list, word_list)

    if after == "":
        r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=headers, allow_redirects=False)
    else:
        r = requests.get(
            'https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None

    after = r.json().get("data").get("after")

    for child in r.json().get("data").get("children"):
        hot_list.append(child.get("data").get("title"))

    return count_words(subreddit, word_list, hot_list, after)
