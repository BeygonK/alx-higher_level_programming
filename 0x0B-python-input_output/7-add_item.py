#!/usr/bin/python3
"""This module defines a function"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


arguments = sys.argv[1:]
filename = "add_item.json"
existing_list = load_from_json_file(filename)
existing_list.extend(arguments)
save_to_json_file(existing_list, filename)
