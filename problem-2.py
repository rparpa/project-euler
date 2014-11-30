#!/usr/bin/python3

# "THE BEER-WARE LICENSE":
# <remi.parpaillon@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Remi Parpaillon


def fibonacci_numbers(limit_max):
    numbers = [1, 2]
    while numbers[0] < limit_max:
        yield numbers[0]
        numbers = [numbers[1], numbers[0] + numbers[1]]

result = 0
for i in fibonacci_numbers(4e6):
    if i & 1:
        result += i

print(result)