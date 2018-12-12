import numpy as np
import pandas as pd
from lxml import objectify


data = pd.read_csv('examples/ex5.csv')
print(data)
# data.to_csv('out.csv', sep='|', na_rep='NULL', index=False, header=False)
#
# import sys
# # data.to_csv(sys.stdout, sep='|')
# data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

# dates = pd.date_range('1/1/2000', periods=7)
# ts = pd.Series(np.arange(7), index=dates)
# ts.to_csv('tseries.csv')
print('---------------------------------')
import csv
with open('examples/ex7.csv') as f:
    # lines = f.read()
    lines = list(csv.reader(f))
header, values = lines[0], lines[1:]
print(header)
print(values)
print(zip(header, zip(*values)))
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)
print('---------------------------------')

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
 {"name": "Katie", "age": 38,
 "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
import json
result = json.loads(obj)
print(result)
asjson = json.dumps(result)
print(asjson)
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

data = pd.read_json('examples/example.json')
print(data)
data.to_json('test_json.json')
data.to_json('test.json', orient='records')

tables = pd.read_html('examples/fdic_failed_bank_list.html')
print(len(tables))
failures = tables[0]
print(failures.head())
close_timestamps = pd.to_datetime(failures['Closing Date'])
print(close_timestamps.dt.year.value_counts())

path = 'mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)

perf = pd.DataFrame(data)
print(perf.head())

from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
print(root)
print(root.get('href'))
print(root.text)


