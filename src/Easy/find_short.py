#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

"""


def find_short(s: str) -> int:
    shortest = float('inf')
    words = s.split()

    for word in words:
        if len(word) < shortest:
            shortest = len(word)

    return shortest
