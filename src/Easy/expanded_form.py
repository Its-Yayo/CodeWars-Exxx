#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/5842df8ccbd22792a4000245

You will be given a number and you will need to return it as a string in Expanded Form. For example:
    expanded_form(12) # Should return '10 + 2'
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.



"""


def expanded_form(num: int) -> str:
    result = str(num)
    list_result = []

    for i, digit in enumerate(result[::-1]):
        if digit != '0':
            list_result.append(digit + '0' * i)

    return ' + '.join(list_result[::-1])