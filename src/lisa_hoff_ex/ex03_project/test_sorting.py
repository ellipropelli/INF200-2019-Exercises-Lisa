#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:20:09 2019

@author: lisahoffstrom
"""

# -*- coding: utf-8 -*-

__author__ = 'Lisa Hoff'
__email__ = 'lisast@nmbu.no'


def bubble_sort(in_data):
    s_data = list(in_data)
    for j in reversed(range(len(s_data))):
        has_changed = False
        for k in range(j):
            if s_data[k+1] < s_data[k]:
                s_data[k], s_data[k+1] = s_data[k+1], s_data[k]
                has_changed = True
        if not has_changed:
            break

    return s_data
