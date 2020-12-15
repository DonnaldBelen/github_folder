import pandas as pd
import json
from collections import Counter
import glob
import os
import csv
import pickle
from os import path

def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x, list):
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

base_path = os.getcwd()
input_dirname = os.path.abspath(os.path.join(base_path,"..","..","input","csv_to_csv"))
filenames = sorted(glob.glob(input_dirname + "/**/*.csv"))

for filename in filenames:
    basename = os.path.basename(filename)
    output_dirname = os.path.abspath(os.path.join(base_path,"..","..","output","csv_to_csv"))
    out_folder = os.path.basename(os.path.abspath(os.path.join(filename,"..")))
    output_dirname = os.path.join(output_dirname,out_folder)
    os.makedirs(output_dirname,exist_ok=True)
    out_filename = os.path.join(output_dirname, basename.replace('.csv', '_parsed_json.csv'))

    with open(filename, 'r') as f:
        data = f.read().split('\n')
    # Flatten JSON to make csv column names
    data = [json.loads(i) for i in data if len(i) != 0]
    flatten_data = [flatten_json(i) for i in data]

    df = pd.DataFrame(flatten_data)

    # Save data as a CSV file
    df.to_csv(out_filename, index=False)
