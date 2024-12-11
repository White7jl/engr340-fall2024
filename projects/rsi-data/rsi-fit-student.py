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

#load data into a dataframe using the pd.read.cvs file because pandas
#is better for loading in csv files
df = pd.read_csv(path_to_file)

#slice data into lists
#load into numpy and pull out the data for each column and create dataframe
#pandas is used because the file was loaded into a dataframe
#we use to.numpy to convert the data frame to an array in numpy so we can
#perform calculations as numpy is better for performing calculations
trial = df['trial'].to_numpy()
force_plate = df['force_plate_rsi'].to_numpy()
accelerometer = df['accelerometer_rsi'].to_numpy()
percent_error = df['percent_error'].to_numpy()

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE
#I used the distribution-fit and histogram-dist example in Mod6 to guide me through this question

#use np.mean and np.std functions for the accelerometer and force_plate data and print the answers
mu_accel = np.mean(accelerometer)
stdev_accel = np.std(accelerometer)
print("The accelerometer mu and STD are" ,mu_accel, "and" ,stdev_accel)

mu_FP = np.mean(force_plate)
stdev_FP = np.std(force_plate)
print("The force_plate mu and STD are" ,mu_FP, "and" ,stdev_FP)

#the start and stop values were found using the max and min values of the data
#the x and y values were found for the force_plate and accelerometer data
#np.linspace is used to plot the data on the x by taking the number of samples
#in the range of the data and norm.pdf finds the distribution
x = np.linspace(start=max(accelerometer), stop=min(accelerometer), num=10000)
y_FP = norm.pdf(x,loc=mu_FP,scale=stdev_FP)

x = np.linspace(start=max(force_plate), stop=min(force_plate), num=10000)
y_accel = norm.pdf(x,loc=mu_accel,scale=stdev_accel)

#the x and y were then plotted for each data set on one graph
#the axis labels, a legend, and title were added and plot lines per each
#dataset were labeled and plotted with a legend included to identify which plot
#line represents which dataset
plt.plot(x,y_accel, label='accelerometer')
plt.plot(x,y_FP, label='force Plate')
plt.title('RSI Distribution of Force Plate and Accelerometer')
plt.xlabel('Probability')
plt.ylabel('Trial')

plt.legend()
plt.show()

"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE
#I used the chi-square-dist-fit example in Mod6 to guide me for this question

#linspace is used to evenly space 9 samples over an interval of 0-2
#np.r_ is used to add bins to account for all values within the interval
bins = np.linspace(0,2,9)
bins = np.r_[-np.inf,bins,np.inf]

#put the accelerometer data into bins that can be computed on a histogram
accel_observed,accel_edges = np.histogram(accelerometer, bins=bins, density=False)

#assign values of 0 and 1 to mu and std because these are our ideal values for mu and std
accel_expected_mu = 0
accel_expected_std = 1

#accel_expected_prob is the probability of getting our expected mu and std values
#accel_expected_counts takes the expected frequency or occurrence of each bin for the length of the dataset
accel_expected_prob = np.diff(norm.cdf(bins, loc=accel_expected_mu, scale=accel_expected_std))
accel_expected_counts= accel_expected_prob*len(accelerometer)

#Conduct Chi2 test the null hypothesis and print the resulting values
#we want to look at the observed vs expected and limit the test to 2 parameters
(chi_stat_accel, p_value_accel) = chisquare(f_obs=accel_observed, f_exp=accel_expected_counts,ddof=2)
print('Chi2 stat for accelerometer data is:', chi_stat_accel, 'p-value for accelerometer data is:', p_value_accel)

#using the recommend alpha value, it was compared against the p_value for the accelerometer
#to determine if the data was or was not a good fit based on if the p_value is lesser or greater than alpha
alpha = 0.05
if p_value_accel < alpha:
    print("The accelerometer data is a good fit")
else:
    print("The accelerometer data is not a good fit")


"""
Force Plate
"""
### YOUR CODE HERE
#all steps used and justified for the accelerometer are repeated and applicable for the force_plate
bins = np.linspace(0,2,9)
bins = np.r_[-np.inf,bins,np.inf]

force_observed,force_edges = np.histogram(force_plate, bins=bins, density=False)

force_expected_mu = 0
force_expected_std = 1

force_expected_prob = np.diff(norm.cdf(bins, loc=force_expected_mu, scale=force_expected_std))
force_expected_counts= force_expected_prob*len(force_plate)

(chi_stat_force, p_value_force) = chisquare(f_obs=force_observed, f_exp=force_expected_counts,ddof=2)
print('Chi2 stat for force_plate data is:', chi_stat_force, 'p-value for force_plate data is:', p_value_force)

alpha = 0.05

if p_value_force < alpha:
    print("The force_plate data is not a good fit")
else:
    print("The force_plate data is good fit")


"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE
#I used the t-test 5.2 Mod  PowerPoint and hypothesis-test Mod5 example to guide me through this

#a t-test is conducted, we need to conduct a two-sided t-test because we are using two independent samples
#(i.e. force_plate and accelerometer) then we print the resulting values

(stat, p_value) = ttest_ind(accelerometer,force_plate, alternative='two-sided')
print("The p-value is", p_value)
print("The stat value is", stat)

#next we use the given alpha to determine if the data is equal or not equal
alpha = 0.05

if p_value < alpha:
    print("The means for the force_plate and accelerometer data are not equal")
else:
    print("The means for the force_plate and accelerometer data are equal")




"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE
#I used the distribution-fit example in Mod6 to guide me through this question
#rsi error can be found by taking the different between the force plate and accelerometer
error = force_plate - accelerometer

#we can plot the error data on a histogram using the given value of 16 bins
#label the x and y-axis and include a title then display the chart
plt.hist(error, bins=16, label='RSI Error')
plt.xlabel('Relative RSI Error')
plt.ylabel('Counts')
plt.title('Distribution of RSI Error')
plt.show()

#we determine mu and std of the error using the np.mean and np.std functions
error_mu = np.mean(error)
error_STD = np.std(error)

(fitted_mean, fitted_std) = norm.fit(error)

#we can use the same logic as previously explained
#number of samples is 10000 to ensure enough samples are taken
#so that a smooth graph is generated
x =  np.linspace(start=-2, stop=2, num=10000)
y = norm.pdf(x, loc=fitted_mean, scale=fitted_std)

#the data is then plotted
plt.plot(x,y, label='Fitted Normal Curve')
plt.title('Fitted Normal Curve of Distribution')
plt.legend()
plt.show()

