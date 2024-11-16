from fileinput import filename

import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
### YOUR CODE HERE
#path to overall file
path_to_file = "C:/Users/jasmi/OneDrive - James Madison University (Dukes)/Desktop/GitHub/engr340-fall2024/data/drop-jump/all_participant_data_rsi.csv"

#load data into a dataframe
df = pd.read_csv(path_to_file)

#slice data into lists
#load into numpy and pull out the data for each column
trial = df['trial'].to_numpy()
force_plate = df['force_plate_rsi'].to_numpy()
accelerometer = df['accelerometer_rsi'].to_numpy()
percent_error = df['percent_error'].to_numpy()


#slice into lists
#use the unique function to automatically pull data
trial = df['trial'].unique()
# convert to a list for easy iteration
trial = trial.tolist()


#repeat for all other columns

force_plate = df['force_plate_rsi'].unique()
force_plate = force_plate.tolist()

accelerometer = df['accelerometer_rsi'].unique()
accelerometer = accelerometer.tolist()

percent_error = df['percent_error'].unique()
percent_error = percent_error.tolist()

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE
#use the mean and std functions for each dataset
mu_accel = np.mean(accelerometer)
stdev_accel = np.std(accelerometer)

mu_FP = np.mean(force_plate)
stdev_FP = np.std(force_plate)

x = np.linspace(start=1.4, stop=0.2, num=1000)
y_FP = norm.pdf(x,loc=mu_FP,scale=stdev_FP)

plt.plot(x,y_FP, label='force Plate')
plt.title('RSI Distribution of Force Plate and Accelerometer')
plt.xlabel('Probability')
plt.ylabel('Trial')

x = np.linspace(start=1.4, stop=0.3, num=1000)
y_accel = norm.pdf(x,loc=mu_accel,scale=stdev_accel)
plt.plot(x,y_accel, label='accelerometer')

plt.legend()
plt.show()

"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), with the 10th bin encompassing [2,inf). An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE
bins = np.linspace(0,2,9)
bins = np.r_[-np.inf,bins,np.inf]

accel_observed,accel_edges = np.histogram(force_plate, bins=bins, density=False)

accel_expected_mu = 0
accel_expected_std = 1

accel_expected_prob = np.diff(norm.cdf(bins, loc=accel_expected_mu, scale=accel_expected_std))
accel_expected_counts= accel_expected_prob*len(force_plate)

#Conduct Chi2 test
(chi_stat, p_value_accel) = chisquare(f_obs=accel_observed, f_exp=accel_expected_counts,ddof=2)

alpha = 0.05
if p_value_accel < alpha:
    print()
else:
    print()


"""
Force Plate
"""
### YOUR CODE HERE
#bins = np.linspace()

#FP_expected =
#FP_observed =

#alpha = 0.05

#(chi_stat, p_value_FP) = chisquare(f_obs=, f_exp=)

#if p_value_FP < alpha:
 #   print()
#else:
  #  print()

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE



#(stat, p_value) = ttest_1samp(,popmean = , alternative='')

#if p_value < alpha:
 #   print()
#else:
#    print()




"""
Question 4 (Bonus): Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE
#error = force_plate - accelerometer

#plt.hist(error, bins=16, label='RSI Error')
#plt.xlabel('Relative RSI Error')
#plt.ylabel('Counts')
#plt.title('Distribution of RSI Error')
#plt.show()

#(fitted_mean, fitted_std) = norm.fit(error)