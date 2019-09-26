# -*- coding: utf-8 -*-

#__author__ = "Lisa Hoff"
#__email__ = "lisahoffstr@gmail.com"

from collections import Counter, defaultdict


def letter_freq(txt):
    # Best solution
    return Counter(txt.lower())


def entropy(message):
    pass


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))