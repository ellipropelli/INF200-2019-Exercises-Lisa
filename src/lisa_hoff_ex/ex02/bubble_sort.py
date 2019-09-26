# -*- coding: utf-8 -*-

__author__ = "Lisa Hoff"
__email__ = "lisast@nmbu.no"


def bubble_sort(data_to_sort):
    n = len(data_to_sort)
    data_sort = list(data_to_sort)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if data_sort[j] > data_sort[j + 1]:
                data_sort[j], data_sort[j + 1] \
                    = data_sort[j + 1], data_sort[j]
    return data_sort


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
