from pkg_resources import require
require('numpy')
import numpy as np
require('matplotlib')
from matplotlib import pyplot as plt
import read_data as rd

fig, ax = plt.subplots()

##################################################################################################################################################
dataset1_77 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',2)
dataset2_77 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',2)           #3528 ~1e6
dataset3_77 = rd.data_read('../cppProcessing2.0/output_reports/09_09_2015_grain_size/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',2)         #background
dataset4_77 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine_small_grain/cs04r-sc-serv-77.diamond.ac.uk/grain_size_test.txt',2)      #small grain

#dataset_77 = rd.combine_data(dataset1_77, dataset2_77)
#dataset_77 = rd.combine_data(dataset_77,dataset3_77)
#dataset_77 = rd.combine_data(dataset_77,dataset4_77)

dataset_77 = dataset3_77 

grain_size77 = np.array(dataset_77[0])
bandwidth77 = np.array(dataset_77[1])
errbar77 = np.array(dataset_77[2])

line1 = ax.plot(grain_size77, bandwidth77, '-r^')

upper77 = errbar77 + bandwidth77
lower77 = bandwidth77 - errbar77
#ax.errorbar(grain_size77, bandwidth77, yerr = [errbar77, errbar77], fmt='r^')
##################################################################################################################################################
dataset1_83 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',2)
dataset2_83 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',2)
dataset3_83 = rd.data_read('../cppProcessing2.0/output_reports/09_09_2015_grain_size/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',2)
dataset4_83 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine_small_grain/cs04r-sc-serv-83.diamond.ac.uk/grain_size_test.txt',2)

dataset_83 = rd.combine_data(dataset1_83, dataset2_83)
dataset_83 = rd.combine_data(dataset_83,dataset3_83)
dataset_83 = rd.combine_data(dataset_83,dataset4_83)

grain_size83 = np.array(dataset_83[0])
bandwidth83 = np.array(dataset_83[1])
errbar83 = np.array(dataset_83[2])

#line2 = ax.plot(grain_size83, bandwidth83, '-g^')

upper83 = errbar83 + bandwidth83
lower83 = bandwidth83 - errbar83
#ax.errorbar(grain_size83, bandwidth83, yerr = [errbar83, errbar83], fmt='g*')
##################################################################################################################################################

dataset1_85 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',2)
dataset2_85 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',2)
dataset3_85 = rd.data_read('../cppProcessing2.0/output_reports/09_09_2015_grain_size/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',2)
dataset4_85 = rd.data_read('../cppProcessing2.0/output_reports/11092015_grain_size_fine_small_grain/cs04r-sc-serv-85.diamond.ac.uk/grain_size_test.txt',2)

dataset_85 = rd.combine_data(dataset1_85, dataset2_85)
dataset_85 = rd.combine_data(dataset_85,dataset3_85)
dataset_85 = rd.combine_data(dataset_85,dataset4_85)

grain_size85 = np.array(dataset_85[0])
bandwidth85 = np.array(dataset_85[1])
errbar85 = np.array(dataset_85[2])

#line3 = ax.plot(grain_size85, bandwidth85, '-b^')

upper85 = errbar85 + bandwidth85
lower85 = bandwidth85 - errbar85
#ax.errorbar(grain_size85, bandwidth85, yerr = [errbar85, errbar85], fmt='b^')
##################################################################################################################################################
ax.set_xlim([30,10e6])
ax.set_xscale('log')
ax.set_ylim([0,3000])
ax.set_yticks(np.arange(0,3000,500))
ax.set_xlabel('Grain Size/elements')
ax.set_ylabel('Bandwidth(MB/s)')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

#plt.legend( [line1[0], line2[0], line3[0]], ['Server 77', 'Server 83', 'Server 85'] )

#plt.savefig('./fig/lineplot_threads.eps', format='eps', dpi=300)
plt.show()

