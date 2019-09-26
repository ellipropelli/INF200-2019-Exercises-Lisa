def letter_freq(txt):
    for letter, count in letter_freq():


if __name__ == '__main__':
    text = input('Hello')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))


