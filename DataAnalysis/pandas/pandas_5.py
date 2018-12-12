import numpy as np
import pandas as pd

pd.options.display.max_rows = 10

# frame = pd.read_csv('examples/ex1.csv')
# print(frame)
# frame.to_pickle('test_pickle')
# print(pd.read_pickle('test_pickle'))

frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('mydata.h5')
# store['obj1'] = frame
# store['obj1_col'] = frame['a']
# print(store)
# print(store['obj1'])
# print(store['obj1_col'])
# store.put('obj2', frame, format='table')
# print(store.select('obj2', where=['index >= 10 and index <= 15']))
# store.close()
#
# frame.to_hdf('mydata.h5', 'obj3', format='table')
# print(pd.read_hdf('mydata.h5', 'obj3', where=['index < 5']))
#
# xlsx = pd.ExcelFile('examples/ex1.xlsx')
# print(pd.read_excel(xlsx, 'Sheet1'))
# print(pd.read_excel('examples/ex1.xlsx', 'Sheet1'))

frame = pd.DataFrame({'a': np.random.randn(100)})
writer = pd.ExcelWriter('ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()

frame.to_excel('ex2_.xlsx')
