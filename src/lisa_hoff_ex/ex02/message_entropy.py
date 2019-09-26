# -*- coding: utf-8 -*-

#__author__ = "Lisa Hof"
#__email__ = "yngve.m.moe@gmail.com"

from collections import Counter, defaultdict


def letter_freq(txt):
    # Best solution
    return Counter(txt.lower())