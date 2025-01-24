#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = next(iter(a_dictionary))
    for x in a_dictionary:
        if a_dictionary[x] > a_dictionary[best]:
            best = x
    return best
