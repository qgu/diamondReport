from pkg_resources import require
require('numpy')
import numpy as np
require('matplotlib')
from matplotlib import pyplot as plt
import read_data as rd

fig, ax = plt.subplots()

##################################################################################################################################################
dataset_77 = rd.data_read('../cppProcessing2.0/output_reports/14092015_threads/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',0)
#dataset1_77 = rd.data_read('../cppProcessing2.0/output_reports/13092015_threads/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',0)

#dataset_77 = rd.combine_data(dataset_77, dataset1_77)

grain_size77 = np.array(dataset_77[0])
bandwidth77 = np.array(dataset_77[1])
errbar77 = np.array(dataset_77[2])

line1 = ax.plot(grain_size77, bandwidth77, '-b*')

upper77 = errbar77 + bandwidth77
lower77 = bandwidth77 - errbar77
#ax.errorbar(grain_size77, bandwidth77, yerr = [errbar77, errbar77], fmt='r^')
##################################################################################################################################################
dataset_83 = rd.data_read('../cppProcessing2.0/output_reports/14092015_threads_large/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',0)
#dataset1_83 = rd.data_read('../cppProcessing2.0/output_reports/13092015_threads/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',0)

#dataset_83 = rd.combine_data(dataset_83, dataset1_83)


grain_size83 = np.array(dataset_83[0])
bandwidth83 = np.array(dataset_83[1])
errbar83 = np.array(dataset_83[2])

line2 = ax.plot(grain_size83, bandwidth83, '-m*')

upper83 = errbar83 + bandwidth83
lower83 = bandwidth83 - errbar83
#ax.errorbar(grain_size83, bandwidth83, yerr = [errbar83, errbar83], fmt='g*')
##################################################################################################################################################

dataset_85 = rd.data_read('../cppProcessing2.0/output_reports/14092015_threads_small/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',0)
#dataset1_85 = rd.data_read('../cppProcessing2.0/output_reports/13092015_threads/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',0)

#dataset_85 = rd.combine_data(dataset_85, dataset1_85)

grain_size85 = np.array(dataset_85[0])
bandwidth85 = np.array(dataset_85[1])
errbar85 = np.array(dataset_85[2])

line3 = ax.plot(grain_size85, bandwidth85, '-k*')

upper85 = errbar85 + bandwidth85
lower85 = bandwidth85 - errbar85
#ax.errorbar(grain_size85, bandwidth85, yerr = [errbar85, errbar85], fmt='b^')
##################################################################################################################################################
ax.set_xlim([0,26])
ax.set_ylim([0,3000])
ax.set_yticks(np.arange(0,3000,500))
ax.set_xticks(np.arange(0,26,1))
ax.set_xlabel('Number of Threads')
ax.set_ylabel('Bandwidth(MB/s)')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.legend( [line1[0], line2[0], line3[0]], ['1058400', '793800', '352800'], loc = 'upper left' )

ax.text(21,100, 'Server 83',
        color='green', fontsize=15)
        
plt.savefig('./fig/lineplot_threads83.eps', format='eps', dpi=300)
plt.show()

