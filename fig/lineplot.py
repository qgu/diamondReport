from pkg_resources import require
require('numpy')
import numpy as np
require('matplotlib')
from matplotlib import pyplot as plt
require('scipy')
from scipy.interpolate import spline


threads = np.arange(1,20)

bandwidth77 = np.array([363.2,682.6,989.7,1.223 * 1024,1.518* 1024,1.68* 1024,1.849* 1024,2.091* 1024,2.172* 1024,2.381* 1024,2.392* 1024,2.347* 1024,2.441* 1024,2.494* 1024,2.657* 1024,2.533* 1024, 2.588*1024,2.525*1024,2.603*1024])
errbar77 = np.array([11.21,11.79,21.42,39.24,37.95,105.7,101.8,110.5, 131.6,230.1,227.1,145.4,125.6,193.2,438.0,165.6,169.8,198.7,163.7])

bandwidth83 = np.array([378.1,749.9,1.023* 1024,1.362* 1024,1.565* 1024,1.825* 1024,1.972* 1024,2.271* 1024,2.268* 1024,2.528* 1024,2.574* 1024,2.504* 1024,2.476* 1024,2.521* 1024,2.552* 1024,2.581* 1024,2.472* 1024,2.492* 1024,2.513* 1024])
errbar83 = np.array([39.89,20.7,42.56,11.12,57.86,94.8,45.44,35.75,132.1,202.7,37.93,118.5,127.9,81.73,53.13,53.78,99.88,71.08,84.54])

bandwidth85 = np.array([389.8, 717.1, 1.007*1024,1.332*1024,1.527*1024,1.804*1024,1.944*1024,2.178*1024,2.343*1024,2.42*1024, 2.486*1024,2.524*1024,2.463*1024,2.501*1024,2.473*1024,2.457*1024,2.432*1024,2.427*1024,2.439*1024])
errbar85 = np.array([1.54,29.83,14.72,15.73,44.26,51.97,58.84,62.14,63.18,65.02,108.4,60.78,82.28,81.12,90.4,117.7,81.77,78.29,61.58])

fig, ax = plt.subplots()

line1 = ax.plot(threads, bandwidth77, '-ro')
line2 = ax.plot(threads, bandwidth85, '-go')
line3 = ax.plot(threads, bandwidth83, '-bo')

upper77 = errbar77 + bandwidth77
lower77 = bandwidth77 - errbar77
ax.errorbar(threads, bandwidth77, yerr = [errbar77, errbar77], fmt='ro')

upper85 = errbar85 + bandwidth85
lower85 = bandwidth85 - errbar85
ax.errorbar(threads, bandwidth85, yerr = [errbar85, errbar85], fmt='go')

upper83 = errbar83 + bandwidth83
lower83 = bandwidth83 - errbar83
ax.errorbar(threads, bandwidth83, yerr = [errbar83, errbar83], fmt='bo')

ax.set_xlim([0,20])
ax.set_xticks(np.arange(0,20,1))
ax.set_yticks(np.arange(0,3500,500))
ax.set_xlabel('No of Threads')
ax.set_ylabel('Bandwidth(MB/s)')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}

plt.legend( [line1[0], line2[0], line3[0]], ['Server 77', 'Server 85', 'Server 83'],loc = 'upper left')
ax.text(13,100, 'grain size = 3528',
        color='green', fontsize=15)

plt.savefig('./fig/lineplot_threads_small_grain.eps', format='eps', dpi=300)
plt.show()


