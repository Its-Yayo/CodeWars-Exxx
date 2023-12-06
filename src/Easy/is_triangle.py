#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/56606694ec01347ce800001b

Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

"""

def is_triangle(a, b, c):
    # Using the triangle inequality problem
    return True if a + b > c and a + c > b and b + c > a else False