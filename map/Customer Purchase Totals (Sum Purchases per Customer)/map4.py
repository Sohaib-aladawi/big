#!/usr/bin/env python
import sys

# Mapper: extract customer ID and purchase amount
for line in sys.stdin:
    try:
        customer_id, amount = line.strip().split(',')
        amount = float(amount)
        # Replace f-string with format() method
        print("{0}\t{1}".format(customer_id, amount))
    except ValueError:
        continue  # Skip lines with errors

