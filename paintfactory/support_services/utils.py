#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Paint Factory Puzzle
# Author: mu.ammad.ud.din@gmail.com
# Last Update: 09 March 2019
# License: MIT


def compareCustomers(a, b):
    if len(b) > len(a):
        return -1
    elif len(a) > len(b):
        return 1

    color_a, end_a = a[0]
    color_b, end_b = b[0]

    if end_a == 1:
        return -1
    elif end_b == 1:
        return 1

    return 0


def compareChoices(a, b):
    color_a, end_a = a
    color_b, end_b = b

    if end_a == 1:
        return 1
    elif end_b == 1:
        return -1

    return 0

def analyzePop(choice, paint):
    color, end = choice

    if choice in paint:
        return True

    if (color, end ^ 1) in paint:
        return False

    return True


def compare_to_key(isCompare):
    'Convert a compare= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return isCompare(self.obj, other.obj) < 0
        def __gt__(self, other):
            return isCompare(self.obj, other.obj) > 0
        def __eq__(self, other):
            return isCompare(self.obj, other.obj) == 0
        def __le__(self, other):
            return isCompare(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return isCompare(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return isCompare(self.obj, other.obj) != 0
    return K