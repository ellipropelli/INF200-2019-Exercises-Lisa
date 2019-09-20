from random import randint as a

__author__ = ''
__email__ = '@nmbu.no'

def generator():
    return randint(1, 6)

def rand_guess():

random_number = generator()
guess_left = 3
flag = 0

while guess > 0:
        guess = int(input('Guess'))
if guess == random_number:
        flag = 1
        break
    else
        print ('wrong guess')

    guess left - = 1

if flag is 1:
    return true
else
    return false

