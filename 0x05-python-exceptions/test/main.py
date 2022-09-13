#!/usr/bin/python3

safe_print_list_integers = __import__('3-safe_print_division.py').safe_print_list_integers

a = 10
b = 5
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, resutlt))
