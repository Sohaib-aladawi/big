#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Mapper: extract year and temperature
for line in sys.stdin:
    try:
        # Assuming CSV format: date, temperature
        date, temperature = line.strip().split(',')
        year = date[:4]  # Extract year from the date
        temperature = float(temperature)
        # Use format method instead of f-string
        print("{0}\t{1}".format(year, temperature))
    except ValueError:
        # Skip lines that don't have the expected format
        continue

