# -*- coding: utf-8 -*-

__author__ = 'Lisa Hoff, Elinor Brede Skårås'
__email__ = 'lisast@nmbu.no, elinor2511@gmail.com'

import random


def roll_dice():
    """
    Returns random number of dice 
    """
    return random.randint(1, 6)


def move_position(position):
    """
    Roll the dice, and moves the position. 
    Checks if the new position is on a ladder or snake and if that´s the case 
    then the position is changed either up or down 
    
    :param position: original position
    :return: new_position: new position after one throw
    """
    ladders_snakes = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                      24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    throw = roll_dice()
    position += throw

    if position in ladders_snakes:
        position = ladders_snakes[position]

    return position


def end_of_game(positions):
    """
    Returns True when one player has reached the goal. (position >= 90)
    :param positions:
    :return: 
    """
    for number in positions:
        if number >= 90:
            return True


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    pass


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    pass


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    pass
