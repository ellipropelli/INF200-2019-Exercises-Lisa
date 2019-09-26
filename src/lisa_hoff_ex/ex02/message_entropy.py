# -*- coding: utf-8 -*-

from collections import Counter
from math import log


def letter_freq(txt):
    # Best solution, added from sample solution.
    return Counter(txt.lower())


def entropy(message):
    letter_count = letter_freq(message)

    n = sum(letter_count.values())
    h = 0

    for number in letter_count.values():
        p = number / n
        h += p * log(p, 2)

    return -h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
