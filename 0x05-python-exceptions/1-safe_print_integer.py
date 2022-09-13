#!/usr/bin/Python3

def safe_print_integer(value):
    try:
        print("{}".format(value))
        return (True)
    except ValueError:
        return (False)
