#!/usr/bin/python3
"""Defines a json file writing function"""

def save_to_json_file(my_obj, filename):
    """write an object to a text file using json representation"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
