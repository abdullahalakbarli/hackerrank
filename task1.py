#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def findarea(self):
        return self.height * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def findarea(self):
        return (self.radius**2) * math.pi


if __name__ == '__main__':  
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
            print(shape.findarea())
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
            print(shape.findarea())
        else:
            raise ValueError("invalid shape type")
