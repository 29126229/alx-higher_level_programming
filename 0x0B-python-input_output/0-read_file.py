tudent.py
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Method that returns directory description '''
        return self.__dict__.copy()dd_item.py
    a script that adds all arguments to a Python list,
    and then save them to a file
'''

from os import path
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    file_path = "add_item.json"
    if path.exists(file_path):
        list_obj = load_from_json_file(file_path)
    else:
        list_obj = list()
    
    tudent.py
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Method that returns directory description with filter '''

        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                res = {}
                for i in attrs:
                    if i in self.__dict__:
                        res[i] = self.__dict__[i]
                return res
        return self.__dict__

    def reload_from_json(self, json):
        ''' Replaces all attributes of the Student instance '''
        fppend_after.py
'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts new_string to a file, after find containing search_string'''
    with open(filename, "r+") as f_object:
        lines = f_object.readlines()
        changed = []
        for line in range(len(lines)):
            changed.append(lines[line])
            if search_string in lines[line]:
                changed.append(new_string)

        f_object.seek(0)
        f_object.write("".join(changed))or attr in json:
            self.__dict__[attr] = json[attr]ave_to_json_file(list_obj + argv, file_path)
    print(end="")!/usr/bin/python3
ad_from_json_file.py
'''

import json


def load_from_json_file(filename):
    ''' creates an Object from a "JSON file" '''

    with open(filename) as f_obj:
        return json.load(f_obj)
m_json_string.py
'''

import json


def from_json_string(my_str):
    ''' returns an object represented by a JSON string '''

    return json.loads(my_str)
on_string.py
'''

import json


def to_json_string(my_obj):
    ''' returns the JSON representation of an object '''

    return json.dumps(my_obj)""0-read_file.py
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """

    with open(filename, 'r', encoding="utf-8") as f_obj:
        content = f_obj.read()
    print(content, end="")
