#!/usr/bin/python3

"""
Instructions: 
Source: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python

Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice


"""

from collections import Counter

def duplicate_count(text: str) -> int:
    # I'll note this so I can remember what I did and what I'm gonna do in the next exercises
    # I lowercase the words and then I returned the sum of how many letters are repeated, using the collections.Counter library method
    # This method basically iterates over the list to store each value then to be compared if there's any equal value.
    
    text_lower = text.lower()
    return sum(1 for count in Counter(text_lower).values() if count > 1)
                