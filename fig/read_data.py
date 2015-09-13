
import re

def data_read(file_name, parameter_position):
	parameter = []
	data = []
	err = []
	f = open(file_name, 'r')
	s = f.readline()
	while s!= '':
		if ']:' in s:
			line = re.split(' |]:|\[|\,',s)
			line = [x for x in line if x != '']
			parameter.append(float(line[parameter_position]))
			if float(line[3])<10:
				data.append(float(line[3])*1024)
			else:
				data.append(float(line[3]))
			err.append(float(line[5]))
			s=f.readline()
	parameter, data, err = zip(*sorted(zip(parameter, data, err)))
	return [parameter, data, err]		

def combine_data(dataset1, dataset2):
	dataset = [0,0,0]
	dataset[0], dataset[1], dataset[2] = zip(*sorted(zip(dataset1[0] + dataset2[0], dataset1[1] + dataset2[1],dataset1[2] + dataset2[2])))
	return dataset
