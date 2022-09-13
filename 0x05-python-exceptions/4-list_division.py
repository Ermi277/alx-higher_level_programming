#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    _res = 0

    for i in range(list_length):
        try:
            _res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            _res = 0
        except TypeError:
            print("wrong type")
            _res = 0
        except IndexError:
            print ("out of range")
            _res = 0
        finally:
            new_list.append(_res)
        return (new_list)
