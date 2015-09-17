from pkg_resources import require
require('numpy')
import numpy as np
require('matplotlib')
from matplotlib import pyplot as plt
import read_data as rd
from matplotlib import gridspec

fig = plt.figure()
gs = gridspec.GridSpec(2, 2)
##################################################################################################################################################
dataset1_77 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',2)           #3528 ~1e6
dataset2_77 = rd.data_read('../cppProcessing2.0/output_reports/09_09_2015_grain_size/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',2)         #background
dataset3_77 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine_small_grain/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',2)      #small grain

grain_size77_1 = np.array(dataset1_77[0])
bandwidth77_1 = np.array(dataset1_77[1])
errbar77_1 = np.array(dataset1_77[2])

grain_size77_2 = np.array(dataset2_77[0])
bandwidth77_2 = np.array(dataset2_77[1])
errbar77_2 = np.array(dataset2_77[2])

grain_size77_3 = np.array(dataset3_77[0])
bandwidth77_3 = np.array(dataset3_77[1])
errbar77_3 = np.array(dataset3_77[2])

ax1 = fig.add_subplot(gs[0,:])
line1 = ax1.plot(grain_size77_2, bandwidth77_2, '-r')
ax3 = fig.add_subplot(gs[1,0])
line1 = ax3.plot(grain_size77_3, bandwidth77_3, '-r')
ax2 = fig.add_subplot(gs[1,1], sharey=ax3)
line1 = ax2.plot(grain_size77_1, bandwidth77_1, '-r')

gs.update(wspace=0.1, hspace=0.25)

#upper77 = errbar77 + bandwidth77
#lower77 = bandwidth77 - errbar77
#ax.errorbar(grain_size77, bandwidth77, yerr = [errbar77, errbar77], fmt='r^')
##################################################################################################################################################
dataset1_83 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',2)           #3528 ~1e6
dataset2_83 = rd.data_read('../cppProcessing2.0/output_reports/09_09_2015_grain_size/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',2)         #background
dataset3_83 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine_small_grain/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',2)      #small grain

grain_size83_1 = np.array(dataset1_83[0])
bandwidth83_1 = np.array(dataset1_83[1])
errbar83_1 = np.array(dataset1_83[2])

grain_size83_2 = np.array(dataset2_83[0])
bandwidth83_2 = np.array(dataset2_83[1])
errbar83_2 = np.array(dataset2_83[2])

grain_size83_3 = np.array(dataset3_83[0])
bandwidth83_3 = np.array(dataset3_83[1])
errbar83_3 = np.array(dataset3_83[2])


line2 = ax1.plot(grain_size83_2, bandwidth83_2, '-g')
line2 = ax2.plot(grain_size83_1, bandwidth83_1, '-g')
line2 = ax3.plot(grain_size83_3, bandwidth83_3, '-g')

#upper83 = errbar83 + bandwidth83
#lower83 = bandwidth83 - errbar83
#ax.errorbar(grain_size83, bandwidth83, yerr = [errbar83, errbar83], fmt='r^')
##################################################################################################################################################
dataset1_85 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',2)           #3528 ~1e6
dataset2_85 = rd.data_read('../cppProcessing2.0/output_reports/09_09_2015_grain_size/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',2)         #background
dataset3_85 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine_small_grain/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',2)      #small grain

grain_size85_1 = np.array(dataset1_85[0])
bandwidth85_1 = np.array(dataset1_85[1])
errbar85_1 = np.array(dataset1_85[2])

grain_size85_2 = np.array(dataset2_85[0])
bandwidth85_2 = np.array(dataset2_85[1])
errbar85_2 = np.array(dataset2_85[2])

grain_size85_3 = np.array(dataset3_85[0])
bandwidth85_3 = np.array(dataset3_85[1])
errbar85_3 = np.array(dataset3_85[2])


line3 = ax1.plot(grain_size85_2, bandwidth85_2, '-b')
#line3 = ax2.plot(grain_size85_1, bandwidth85_1, '-b')
#line3 = ax3.plot(grain_size85_3, bandwidth85_3, '-b')

#upper85 = errbar85 + bandwidth85
#lower85 = bandwidth85 - errbar85
#ax.errorbar(grain_size85, bandwidth85, yerr = [errbar85, errbar85], fmt='r^')
##################################################################################################################################################
ax1.set_xlim([300,5e6])
ax1.set_xscale('log')

ax2.set_xlim([1e4, 2e6])
ax2.set_xscale('log')

ax3.set_xlim([30,3528*2])
ax3.set_xscale('log')

ax1.set_ylim([0,3000])
ax1.set_yticks(np.arange(0,3000,500))
ax2.set_ylim([0,3000])
plt.setp(ax2.get_yticklabels(), visible=False)

ax3.set_ylim([0,3000])
ax3.set_yticks(np.arange(0,3000,500))

ax1.set_xlabel('Grain Size/elements')
ax2.set_xlabel('Grain Size/elements')
ax3.set_xlabel('Grain Size/elements')

ax1.set_ylabel('Bandwidth(MB/s)')
ax2.set_ylabel('')
ax3.set_ylabel('Bandwidth(MB/s)')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

ax1.legend( [line1[0], line2[0], line3[0]], ['Server 77', 'Server 83', 'Server 85'] )

plt.savefig('./fig/lineplot_grain_size.png', format='png', dpi=300)
plt.show()

