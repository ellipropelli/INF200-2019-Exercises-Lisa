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


    def test_empty():
        """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []
    assert bubble_sort(()) == []



def test_single():
    """Test that the sorting function works for single-element list"""
    pass


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    pass


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    pass


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    pass


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass