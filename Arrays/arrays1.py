#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:44:28 2021

@author: john
"""

# find max hourglass sum 3 X 1 X 3

import numpy as np
import sys

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

answer = -(sys.maxsize - 1)

for y in range(0, 3):
    for x in range(0, 4):
        temp = sum(arr[y][x:x+3]) + arr[y + 1][x + 1] + sum(arr[y + 2][x:x+3])
        print(y, " ", x)
        answer = temp if temp > answer else answer
#
# print(answer)