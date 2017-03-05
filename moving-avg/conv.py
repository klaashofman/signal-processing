# moving average example by using convolution
# 
# 
# http://stackoverflow.com/questions/13728392/moving-average-or-running-mean/27681394#27681394

import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(1000)
N=100
avg = np.convolve(x, np.ones((N,))/N, mode='same')
print avg
plt.plot(x, 'k+', label='random normalised')
plt.plot(avg, 'b-', label='average')
plt.legend()
plt.show()
