#!/usr/bin/python3

# "THE BEER-WARE LICENSE":
# <remi.parpaillon@gmail.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Remi Parpaillon

total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)