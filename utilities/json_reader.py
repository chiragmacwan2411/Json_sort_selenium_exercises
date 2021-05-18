import json

"""
       utility method to read json file and return python dict
"""
def json_data_reader(json_file_path):
    try:
        with open(json_file_path) as f:
            data = json.load(f)
        return data
    except OSError:
        print("file can not be found :: " + json_file_path)



"""
        reads the value of given key from given dict
"""
def json_data_key_reader(json_file_path, key):
    json_data = json_data_reader(json_file_path)
    return json_data[key]



"""
        returns json from given python dict 
"""
def json_dumper(jsn):
    return json.dumps(jsn, indent=2)
