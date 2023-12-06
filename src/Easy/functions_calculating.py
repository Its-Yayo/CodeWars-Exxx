#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

This time we want to write calculations using functions and get the results. Let's have a look at some examples:
    seven(times(five())) # must return 35
    four(plus(nine())) # must return 13
    eight(minus(three())) # must return 5
    six(divided_by(two())) # must return 3

Requirements:
    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

    eight(divided_by(three()))

"""

def zero(func=None): return 0 if func is None else func(0)
def one(func=None): return 1 if func is None else func(1)
def two(func=None): return 2 if func is None else func(2)
def three(func=None): return 3 if func is None else func(3)
def four(func=None): return 4 if func is None else func(4)
def five(func=None): return 5 if func is None else func(5)
def six(func=None): return 6 if func is None else func(6)
def seven(func=None): return 7 if func is None else func(7)
def eight(func=None): return 8 if func is None else func(8)
def nine(func=None): return 9 if func is None else func(9)

def plus(x): return lambda y: y + x
def minus(x): return lambda y: y - x
def times(x): return lambda y: y * x
def divided_by(x): return lambda y: y // x