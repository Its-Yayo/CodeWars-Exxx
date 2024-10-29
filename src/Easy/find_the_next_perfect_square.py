#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/56269eb78ad2e4ced1000013/solutions/python

Write a function, persistence, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect 
square after the one passed as a parameter. Recall that an integral perfect 
square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an 
empty value like None or null, depending on your language. You may assume the argument 
is non-negative.

Examples ( Input --> Output )
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square

"""

from math import sqrt

def find_next_square(sq: int) -> int:
    return -1 if not sqrt(sq).is_integer() else (sqrt(sq) + 1) ** 2 
    