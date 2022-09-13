#!/usr/bin/python3

def safe_print_division(a, b):
    _res = 0

    try:
        _res = a / b
    except:
        _res = None
    finally:
        print("Inside Result {}".format(_res))
    return (_res)
