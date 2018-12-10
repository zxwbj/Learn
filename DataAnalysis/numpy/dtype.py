import numpy as np

dt = np.dtype(np.int32)
print(dt)

dt = np.dtype('i4')
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
print(dt)

dt = np.dtype([('age', np.int8)])
print(dt)

a = np.random.random(4)
print(a)
print(a.dtype)
print(a.shape)
