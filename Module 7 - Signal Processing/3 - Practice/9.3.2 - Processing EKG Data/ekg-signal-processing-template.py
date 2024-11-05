import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

#signal = 0
## YOUR CODE HERE ##
signal = np.loadtxt(signal_filepath, skiprows=2, delimiter=",")

column_one = signal[:,0]            ## Time in seconds
column_two = signal[:,1]            ## MLII
column_three = signal[:,2]          ## V5

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##
#np.convolve()

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##

differ2= np.diff(column_two)
differ3 = np.diff(column_three)

"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
square2 = np.square(differ2)
square3 = np.square(differ3)

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
filter2 = np.square(np.diff(square2))
filter3 = np.square(np.diff(square3))

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.xlabel('Time (s)')
plt.ylabel('Raw Signal Amplitude')
plt.plot(column_one,column_three)
plt.plot(column_one,column_two)
plt.show()

plt.title('Process Signal for ' + database_name)
plt.xlabel('Time (s)')
plt.ylabel('Differentiated Signal Amplitude')
plt.plot(column_one[1:],differ3)
plt.plot(column_one[1:],differ2)
plt.show()

plt.title('Process Signal for ' + database_name)
plt.xlabel('Time (s)')
plt.ylabel('Squared Signal Amplitude')
plt.plot(column_one[1:],square3)
plt.plot(column_one[1:],square2)
plt.show()

plt.title('Process Signal for ' + database_name)
plt.xlabel('Time (s)')
plt.ylabel('Filtered Signal Amplitude')
plt.plot(column_one[2:],filter3)
plt.plot(column_one[2:],filter2)
plt.show()
