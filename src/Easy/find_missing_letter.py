#!/usr/bin/python3

"""
Instructions:
Source:

Find the missing letter Write a method that takes an array of consecutive (increasing) letters as input and that
returns the missing letter in the array.

You will always get a valid array. And it will be always exactly one letter be missing. The length of the array will
always be at least 2. The array will always contain letters in only one case.

Example:

    ['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'

"""

def find_missing_letter(chars: list[str]) -> str:
    # Init approach will take all the ASCII int values
    # It will transverse the array from start to end the sum of all the elements
    # It will return the subtraction of the subtotal and the sum of the array (ints)
    # Just it takes the first and last element of the array to avoid ASCII range errors

    ints = [ord(char) for char in chars]
    n = len(ints)

    total = (n + 1) * (ints[0] + ints[-1]) / 2
    ints_sum = sum(ints)

    total_number = total - ints_sum

    return chr(int(total_number))
