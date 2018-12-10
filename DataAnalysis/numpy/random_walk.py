import random
import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

print(walk)

# plt.plot(walk[:100])
# plt.show()
print('----------------------------------------')

import numpy as np
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
print(steps)
print(walk)
print(walk.min())
print(walk.max())
print(np.abs(walk) >= 10)
print((np.abs(walk) >= 10).argmax())
print('-----------------------------------------')
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(axis=1)
print(walks.max())
print(walks.min())

hits30 = (np.abs(walks) >= 30).any(axis=1)
print(hits30.shape)
print(hits30.sum())
print(hits30)
print(walks)

print((walks[hits30]))                  # boolean indexing
print((walks[hits30]).shape)

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)
print(crossing_times)
print(crossing_times.mean())

