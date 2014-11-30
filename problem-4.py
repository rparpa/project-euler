#!/usr/bin/python3

# "THE BEER-WARE LICENSE":
# <remi.parpaillon@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Remi Parpaillon
import math


def is_palindrome(number):
    number_string = str(number)
    for digit_pos in range(0, math.floor(len(number_string) / 2)):
        if number_string[digit_pos] != number_string[-1 - digit_pos]:
            return False
    return True


