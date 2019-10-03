# -*- coding: utf-8 -*-

__author__ = 'Lisa Hoff'
__email__ = 'lisast@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))

def test_single():
    """i: A test that the median function returns the correct value for a
    one-element list"""
    assert median([5]) == 5


def test_odd_num_elements():
    """ii: Test median for lists with odd number of elements."""
    assert median([3, 1, 2]) == 2
    assert median([3, 1, 2, 3, 5]) == 3


def test_even_num_elements():
    """ii: Test median for lists with even number of elements."""
    assert median([3, 1, 2, 4]) == 2.5
    assert median([3, 2, 1, 4, 3, 5]) == 3


def test_ordered_elements():
    """ii: Test median for list with ordered elements."""
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5