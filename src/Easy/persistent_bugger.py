#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/solutions/python

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)


"""


from math import prod

def persistence(init_number: int) -> int:
    cont = 0
    
    while init_number >= 10:
        # Multiplication thing
        digits = [int(d) for d in str(init_number)]
        multiplication_number = prod(digits)
        
        init_number = multiplication_number
        cont += 1
        
    return cont