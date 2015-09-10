from pkg_resources import require
require('numpy')
import numpy as np
require('matplotlib')
from matplotlib import pyplot as plt

fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

N = 13
bandwidth   = (44.61,128,197,217, 233.7,425,669,777, 1650,1760,1300,1923, 2280)
ind = np.arange(1, N+1)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.barh(-ind, bandwidth,   width, color='r')

labels = ('Baseline', 'Parallelised', 'Variable Reuse', 'Bitwise', 'Avoiding Dereference','TBB Pipiline', 'More Bitwise', 'Set grain_size', '-O3 -no-SSE', '-O3 only','AVX(unaligned) pipeline','AVX(aligned) pipeline', 'AVX(aigned) parallel_for')

plt.xlabel('Bandwidth(MB/s)')
#locs, labels = plt.xticks(ind-width/3.,  )
#plt.setp(labels,  rotation=40)

plt.xticks(np.arange(0,3500,500))
plt.yticks(-ind, labels)
plt.ylim([-N-1,0])

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)

ax = fig.add_subplot(111)

for x in ind:
	ax.text(bandwidth[x-1] + 50, -ind[x-1], '{0:}x'.format(int(bandwidth[x-1]/bandwidth[0])), fontsize=14, color='blue')

plt.gcf().subplots_adjust(left=0.35)

plt.savefig('./fig/barplot.eps', format='eps', dpi=300)
plt.show()
