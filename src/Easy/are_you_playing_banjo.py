#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/53af2b8861023f1d88000832

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

    name + " plays banjo"
    name + " does not play banjo"

Names given are always valid strings.
"""

def are_you_playing_banjo(name: str) -> str:
    # Just to practice lmao
    return f'{name} plays banjo' if name[0] == 'r' or name[0] == 'R' else f'{name} does not play banjo'
