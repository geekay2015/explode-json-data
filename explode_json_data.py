# -*- coding: utf-8 -*-
#
# Script Name		: explode_json_data.py
#
# Author		    : Gangadhar Kadam
# Created		    : 16 Aug 2018
# Version		    : 1.0
#
# Description	    : Exploding the nested json dictionaries and list

# Import the modules
from __future__ import print_function
import json


class NotADictionary(Exception):
    """
    A class used to throw an exception when the json
    object is not a dictionary
    """
    pass


class EmptyDictionary(Exception):
    """
    A class used to throw an exception when the json
    object is empty
    """
    pass


def flatten(obj: dict) -> dict:

    """
    This function takes a dictionary with arbitrary levels of nested
    lists and dictionaries and flattens it.

    Raises NotADictionary if the input is invalid.
    """

    # check if the object is dictionary
    if not isinstance(obj, dict):
        raise NotADictionary

    # check if the dictionary is empty
    if not bool(dict):
        raise EmptyDictionary

    # create empty output data dictionary
    exploded_data = {}

    # explode function
    def explode_json(json_data, name=''):
        # check if the object type is a dictionary
        if type(json_data) is dict:
            for key in json_data:
                # if the dict is empty
                if not bool(json_data[key]):
                    exploded_data[name + key + '.'[:-1]] = json_data[key]
                else:
                    explode_json(json_data[key], name + key + '.')

        # check if the object type is a dictionary
        elif type(json_data) is list:
            i = 0
            for key in json_data:
                explode_json(key, name + str(i) + '.')
                i += 1
        else:
            exploded_data[name[:-1]] = json_data

    try:
        explode_json(obj)

    except Exception as e:
        raise e

    return exploded_data


# function to read Json as a dictionary
def read_json(filename):
    with open(filename) as f:
        return json.load(f)


if __name__ == '__main__':
    # define the input file path
    input_file = "/Users/gangadharkadam/PycharmProjects/parse-json-data/woodchuk.json"

    # read json as dictionary
    wood_chuck_data = read_json(input_file)

    # print the original json
    # print(wood_chuck_data)

    # explode the input json
    print(flatten(wood_chuck_data))




