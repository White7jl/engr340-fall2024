import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
#pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1.0
b = 1.0/math.sqrt(2.0)
t = 0.25
p = 1.0

# perform 10 iterations of this loop
for i in range(1,10):
    a1 = (a+b)/2.0
    b1 = math.sqrt(a*b)
    t1 = ((t-p)*(a1-a)**2.0)
    p1 = 2.0*p
    a = a1
    b = b1
    t = t1
    p = p1

    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i, ((a + b)**2 /4*t))

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = (((a+b)**2)/4*t)


print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
