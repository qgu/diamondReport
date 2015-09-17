from pkg_resources import require
require('numpy')
import numpy as np
require('matplotlib')
from matplotlib import pyplot as plt
require('scipy')
from scipy.interpolate import spline


alignment = np.array([32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])

bandwidth77 = np.array([3.096,3.072,3.019,2.946,2.936,2.864,2.626])
bandwidth83 = np.array([2.729,2.817,2.891,2.582,2.801,2.922,2.824])
bandwidth85 = np.array([2.678,2.760,2.766,2.626,2.717,2.723,2.558])

bandwidth1_77 = np.array([2.874,2.929,3.176,2.857,2.950,2.860,3.156,3.034,2.990])
bandwidth1_83 = np.array([2.738,2.766,2.729,2.830,2.779,2.751,2.834,2.867,2.779])
bandwidth1_85 = np.array([2.732,2.681,2.433,2.687,2.782,2.757,2.649,2.776,2.438])

fig, ax = plt.subplots()

line1 = ax.plot(alignment, bandwidth1_77*1024, '-ro')
line2 = ax.plot(alignment, bandwidth1_85*1024, '-go')
line3 = ax.plot(alignment, bandwidth1_83*1024, '-bo')

ax.set_xlim([0,10000])
ax.set_xscale('log')
#ax.set_xticks(np.arange(0,10000,100))
ax.set_yticks(np.arange(0,3500,500))
ax.set_xlabel('Alignment')
ax.set_ylabel('Bandwidth(MB/s)')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.legend( [line1[0], line2[0], line3[0]], ['Server77', 'Server 85', 'Server 83'],loc = 'upper left')
ax.text(13,100, 'grain size = 3528',
        color='green', fontsize=15)

#plt.savefig('./fig/lineplot_alignment.eps', format='eps', dpi=300)
plt.show()


