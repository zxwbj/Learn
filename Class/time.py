import time

time0 = time.time()
s = ''
for i in range(1000000):
    s += 'tst'
time1 = time.time()
l = ['tst' for i in range(1000000)]
s = ''.join(l)
time2 = time.time()
L = []
for i in range(1000000):
    L.append('tst')
s = "".join(L)
time3 = time.time()
s = 'tst' * 1000000
time4 = time.time()

print(time1 - time0)
print(time2 - time1)
print(time3 - time2)
print(time4 - time3)


