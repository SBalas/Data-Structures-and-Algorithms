# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:23:12 2021

@author: sibalas
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2  # ** means power of
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    # print the objects of the class
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


c1 = Coordinate(3, 8)
c2 = Coordinate(7, 3)

print("Coords of c1:", c1.x, c1.y)
print("Coords of c2:", c2.x, c2.y)

# uses the str function in the class
print(c1, c2)

# Two ways to get the distance between c1 and c2
print(c1.distance(c2))
print(Coordinate.distance(c1, c2))
print("\n")

# Class to create and run fractions

class Fraction:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    # function to print in fraction form
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    # function to add two fractions
    def __add__(self, other):
        newnum = self.num * other.denom + \
                 self.denom * other.num
        newdenom = self.denom * other.denom
        common = gcd(newnum, newdenom)
        return Fraction(newnum//common, newdenom//common)   # // gives int, / gives float

    # Deep equality when f1 and f2 have different reference but mathematicall equal
    # Shallow equality when both f2 and f2 point to same reference
    # This is a function for deep equality (1/2 and 2/4) --- check whether 1*4 == 2*2
    def __eq__(self, other):
        firstnum = self.num * other.denom
        secondnum = other.num * self.denom

        return firstnum == secondnum

# function to calculate the gretest common divisor
# if (m,n) don't divide directly, then GCD is (n, m%n) and so on
# Example: GCD(15,10) = GCD(10, 5) = 5

def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

f1 = Fraction(1,4)
f2 = Fraction(2,6)

print(f1)
print(f2)
print(f1 + f2)
print(f1 == f2)
