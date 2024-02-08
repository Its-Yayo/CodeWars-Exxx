#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/583710ccaa6717322c000105

This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

"""

def simple_multiplication(number: int) -> int :
    return number * 8 if number % 2 == 0 else number * 9