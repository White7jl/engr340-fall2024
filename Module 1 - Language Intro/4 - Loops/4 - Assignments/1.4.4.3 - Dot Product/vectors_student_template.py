import random
import numpy as np


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)

    # return the generated list
    return randoms

def dot_product(va,vb):  ##finding the dot product of 2 vectors
    dot_product = 0
    for n in range(len(va)):
        dot_product += (va[n] * vb[n])

    return dot_product

"""
Step 1: Generate two "vectors" of equal length but full of random values
"""
max_length = 10
maximum_value = 100
fixed_length = int(random.uniform(2, max_length))
vector_a = generate_random_int_list(fixed_length, maximum_value)
vector_b = generate_random_int_list(fixed_length, maximum_value)

"""
Step 2: Iterate through the vector(s) and calculate the dot product
"""

# store your result here. Do not change the name
dot_product = dot_product(vector_a,vector_b)

### Your code here
##alternatively
## for i in range(len(vector_a)):
##  dot_product += (vector_a[i]*vector_b[i])

"""
Step 3:
Calculate the error of your dot_product compared with numpy's solution
"""
# check code with numpy...
a_np = np.asarray(vector_a)
b_np = np.asarray(vector_b)

# use dot product from numpy to check this result
correct = np.dot(a_np, b_np)
error = correct - dot_product

# compare results
print("Your result: ", dot_product)
print("Correct result: ", correct)
print("Error: ", error)
