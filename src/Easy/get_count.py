#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/54ff3102c1bad923760001f3/

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

"""

def get_count(string: str) -> str:
    # Approach that will make a dict comprehension in order to count every vowel in the str
    # It returns the sum of all those vowels
    vowels = 'aeiou'
    vowel = {vowel: string.count(vowel) for vowel in vowels}

    return sum(vowel.values())