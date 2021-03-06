import json
import pydoc
import os
import sys

def metadata():
    json_file = os.path.join(os.path.dirname(__file__), '../source/pytorch-metadata.json')
    json_data = open(json_file).read()
    json_root = json.loads(json_data)

    schema_map = {}

    for schema in json_root:
        name = schema['name']
        schema_map[name] = schema

    for schema in json_root:
        name = schema['name']
        if 'module' in schema:
            class_name = schema['module'] + '.' + name
            # print(class_name)
            class_definition = pydoc.locate(class_name)
            if not class_definition:
                raise Exception('\'' + class_name + '\' not found.')
            docstring = class_definition.__doc__
            if not docstring:
                raise Exception('\'' + class_name + '\' missing __doc__.')
            # print(docstring)

if __name__ == '__main__':
    command_table = { 'metadata': metadata }
    command = sys.argv[1]
    command_table[command]()
