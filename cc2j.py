""" cc2j will convert a CSV to JSON """
import csv
import json
from tqdm import tqdm

jsonfile = open('output.json', 'w')

with open('input.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data_rows = []
    
    for row in tqdm(csv_reader):
        data_rows.append(row)
    
    json.dump(data_rows, jsonfile, indent = 4, ensure_ascii = False)
    jsonfile.write('\n')
