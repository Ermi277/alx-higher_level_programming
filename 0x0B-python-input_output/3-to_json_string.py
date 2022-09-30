#!/usr/bin/python3
"""Defines a to json string function"""
import json


def to_json_string(my_obj):
    """Return the json represntation of a string object"""

    return json.dumps(my_obj)
