#!/usr/bin/env python
import sys

current_customer = None
total_amount = 0.0

# Reducer: sum purchases per customer
for line in sys.stdin:
    customer_id, amount = line.strip().split('\t')
    amount = float(amount)
    
    if current_customer == customer_id:
        total_amount += amount
    else:
        if current_customer is not None:
            # Output result for the previous customer using format()
            print("{0}\t{1}".format(current_customer, total_amount))
        current_customer = customer_id
        total_amount = amount

# Output the final customer's result
if current_customer is not None:
    print("{0}\t{1}".format(current_customer, total_amount))

