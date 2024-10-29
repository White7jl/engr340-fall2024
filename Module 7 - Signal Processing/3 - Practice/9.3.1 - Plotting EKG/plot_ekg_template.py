
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###

my_EKG_Data = np.loadtxt(path, skiprows=2, delimiter=",")

# save each vector as own variable

### Your code here ###


Column_one = my_EKG_Data[:,0]            ## Time in seconds
Column_two = my_EKG_Data[:,1]            ## MLII
Column_three = my_EKG_Data[:,2]          ## V5

# use matplot lib to generate a single

### Your code here ###
plt.title('EKG Data')
plt.xlabel('Time (s)')
plt.ylabel('V5')
plt.plot(Column_one,Column_three)
plt.plot(Column_one,Column_two)
plt.show()
