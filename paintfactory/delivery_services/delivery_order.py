#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Paint Factory Puzzle
# Author: mu.ammad.ud.din@gmail.com
# Last Update: 09 March 2019
# License: MIT


def deliverOrder(paint, nPaintColors, customerId):
    
    result = "Case #{}: ".format(customerId)
    if not paint:
        result += "IMPOSSIBLE"
    else:
        arr = [("1" if (i, 1) in paint else "0") for i in range(1, nPaintColors + 1)]
        result += ' '.join(arr)

    return result
