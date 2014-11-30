#!/usr/bin/python3

# "THE BEER-WARE LICENSE":
# <remi.parpaillon@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Remi Parpaillon


def prime_numbers(limit):
    number = 3
    primes = [2, number]
    is_number_prime = True

    yield 2
    while number <= limit:
        if is_number_prime:
            primes.append(number)
            yield number

        number += 2

        is_number_prime = True

        for a in primes:
            if number % a == 0:
                is_number_prime = False
                break


def get_prime_divisor(number):
    for i in prime_numbers(number / 2):
        if number % i == 0:
            print('Prime divisor : %d' % i)

get_prime_divisor(int(input('For which number do you want to find its greatest prime divisor ? : ')))