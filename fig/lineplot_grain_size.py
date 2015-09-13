from pkg_resources import require
require('numpy')
import numpy as np
require('matplotlib')
from matplotlib import pyplot as plt


grain_size = np.array([3528/7,3528/6, 3528/4, 3528/3,3528/2,3528,3528*3, 3528*7,3528*9, 3528*21, 3528*59, 3528*63, 3528*177,3528*413,3528*531,3528*1239])

bandwidth77 = np.array([2.834,2.646,2.698,2.565,2.565,2.499,2.462,2.538,2.167,2.152,1.329,1.351,1.048,929.6/1024, 555.3/1024,487.4/1024])*1024
bandwidth83 = np.array([2.702,2.572,2.770,2.702,2.716,2.491,2.406,2.519,2.375,2.483,1.895,1.950,1.796,1.408,836.3/1024,525.5/1024])*1024
bandwidth85 = np.array([2.664,2.642,2.603,2.687,2.626,2.460,2.386,2.443,2.316,2.310,1.797,1.829,1.626,1.229,796.2/1024,525.4/1024])*1024

NoOfThreads83 = np.array([10,10,10,10,10, 10,10,10,10,10, 10,10,10, 9, 8, 3])

errbar77 = np.array([344.8,198.6,188.0,245.9,200.3,96.00,152.3,161.8,205.1,144.0,78.90,117.9,83.58,42.84,35.37,20.51])
errbar83 = np.array([136.8,94.62,163.5,117.0,82.48,25.25,61.67,101.1,62.11,162.1,55.34,67.18,77.70,96.59,19.42,13.71])
errbar85 = np.array([89.68,103.0,119.7,140.6,85.58,133.4,85.37,78.85,51.83,93.97,67.33,62.76,75.70,50.05,52.14,16.30])

fig, ax = plt.subplots()

line1 = ax.plot(grain_size, bandwidth77, '-ro')
line2 = ax.plot(grain_size, bandwidth83/NoOfThreads83, '-g^')
line3 = ax.plot(grain_size, bandwidth85, '-b*')

upper77 = errbar77 + bandwidth77
lower77 = bandwidth77 - errbar77
ax.errorbar(grain_size, bandwidth77, yerr = [errbar77, errbar77], fmt='ro')

upper83 = errbar83 + bandwidth83
lower83 = bandwidth83 - errbar83
ax.errorbar(grain_size, bandwidth85, yerr = [errbar83, errbar83], fmt='g*')

upper85 = errbar85 + bandwidth85
lower85 = bandwidth85 - errbar85
ax.errorbar(grain_size, bandwidth83/NoOfThreads83, yerr = [errbar85, errbar85], fmt='b*')

ax.set_xlim([300,3528*3717])
ax.set_xscale('log')
ax.set_ylim([0,3000])
ax.set_yticks(np.arange(0,3000,500))
ax.set_xlabel('Grain Size/elements')
ax.set_ylabel('Bandwidth(MB/s)')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.legend( [line1[0], line2[0], line3[0]], ['Server 77', 'Server 83', 'Server 85'] )


#plt.savefig('./fig/lineplot_threads.eps', format='eps', dpi=300)
plt.show()





