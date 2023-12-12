#!/usr/bin/python3


def find_missing_letter(chars: list[str]) -> str:
    # Init approach will take all the ASCII int values
    # It will transverse from start to end the sum of all the elements
    # It will return the substraction of the subtotal and the sum of the array (ints)
    # Just it takes the first and last element of the array to avoid ASCII range errors

    ints = [ord(char) for char in chars]
    n = len(ints)

    total = (n + 1) * (ints[0] + ints[-1]) / 2
    ints_sum = sum(ints)

    total_number = total - ints_sum

    return chr(int(total_number))