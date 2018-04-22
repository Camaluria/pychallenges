#!/usr/bin/python3
"""
Challenge 1
Cameron Alexander
Write a progam which will find all such numbers which are divisible by 7, but
are not a multiple of 5, between 2000 and 3200 (both included)
"""

for number in range(2000,3201):
    if (number % 7 == 0) and (number % 5 != 0) :
        print(number)
