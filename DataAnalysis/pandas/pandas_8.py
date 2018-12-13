import numpy as np
import pandas as pd
import re

text = "foo bar\t baz \tqux"
print(text)
print(re.split('\s+', text))
regex = re.compile('\s+')
print(regex.split(text))
print(regex.findall(text))

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex)
print(regex.findall(text))

m = regex.search(text)
print(m)
print(text[m.start():m.end()])
print(regex.match(text))
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@bright.net')
print(m.groups())
print(regex.findall(text))
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))
print('-------------------------------------------------------')

data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
print(data)
data = pd.Series(data)
print(data)
print(data.isnull())
print(data.str.contains('gmail'))
print(pattern)
print(data.str.findall(pattern, flags=re.IGNORECASE))
matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)
print(matches.str.get(1))
print(matches.str[0])
print(data.str[:5])

