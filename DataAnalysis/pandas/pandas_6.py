import numpy as np
import pandas as pd
# import requests

# url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
# resp = requests.get(url)
# print(resp)
# data = resp.json()
# print(data[0]['title'])
# issues = pd.DataFrame(data, columns=['number', 'events_url'])
# print(issues)

import sqlite3

query = """CREATE TABLE test
            (a VARCHAR(20), b VARCHAR(20),
             c REAL,        d INTEGER);"""
con = sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()
cursor = con.execute('select * from test')
rows = cursor.fetchall()
print(rows)
print(cursor.description)
print(pd.DataFrame(rows, columns=[x[0] for x in cursor.description]))

import sqlalchemy as sqla

db = sqla.create_engine('sqlite:///mydata.sqlite')
print(pd.read_sql('select * from test', db))
