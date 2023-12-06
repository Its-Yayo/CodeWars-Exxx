#!/usr/bin/python3

"""
Instructions:
Source: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


def find_uniq(arr: list[int]) -> int:
    # Function that will iterate through the array and it will compare first 2 values
    # If they are different, it will return the value just if if it's different from the 3, 4.. n value
    # If not, it will return the 2 value
    # It returns the last value in case of an Index out of range exception
    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            try:
                return arr[i] if arr[i] != arr[i + 2] and i < len(arr) - 2 else arr[i + 1]
            except IndexError:
                return arr[-1]



