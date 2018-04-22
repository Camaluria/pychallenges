#!/usr/bin/python3
"""
Challenge 3
Cameron Alexander
Write a progam which uses map() and filter() to make a list who elements are
square of an even number

Hint:
Use map()
use lambda()
use filter()
"""

def fill_list(l):
    for i in range (0,101):
        l.append(i)

base_numbers = []
fill_list(base_numbers)

even_squares = list(map(lambda x: x**2, filter(lambda x: x%2 == 0, base_numbers)))

print(even_squares)
