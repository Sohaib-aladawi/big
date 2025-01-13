#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

current_year = None
max_temp = float('-inf')

# Reducer: find max temperature per year
for line in sys.stdin:
    year, temp = line.strip().split('\t')
    temp = float(temp)
    
    if current_year == year:
        max_temp = max(max_temp, temp)
    else:
        if current_year is not None:
            # Output result for the previous year using format method
            print("{0}\t{1}".format(current_year, max_temp))
        current_year = year
        max_temp = temp

# Output the final year’s result
if current_year is not None:
    print("{0}\t{1}".format(current_year, max_temp))

