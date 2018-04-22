#!/usr/bin/python3
"""
Challenge 2
Cameron Alexander
Write a progam which takes a user input and compute the factorial of a given
number
"""

def factorial_calc(num):
    if num == 0:
             return 1
    else:
        return num * factorial_calc(num - 1)


number = int(input("Please insert a number: "))

print(factorial_calc(number))
