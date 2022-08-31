#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    bet = list(a_dictionary.keys())[0]
    grt = a_dictionary[bet]
    for k, i in a_dictionary.items():
        if v > grt:
            bet = k
    return (bet)
