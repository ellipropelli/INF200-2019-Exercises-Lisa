# -*- coding: utf-8 -*-

__author__ = "Lisa Hoff"
__email__ = "lisast@nmbu.no"


def char_counts(textfilename):
    textfile = open(textfilename)
    stringtxt = textfile.read()
    textfile.close()
    # stringtxt = stringtxt.lower()
    count_charac = {}

    for key in range(256):
        count_charac[key] = 0

    for index, char in enumerate(stringtxt):
        if ord(char) in count_charac.keys():
            count_charac[ord(char)] += 1
        else:
            count_charac[ord(char)] = 1
    return count_charac


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]))
