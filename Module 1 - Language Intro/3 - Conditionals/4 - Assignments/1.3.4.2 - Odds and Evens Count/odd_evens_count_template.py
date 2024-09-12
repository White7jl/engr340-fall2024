# bring in randomness cause we need it in our lives
import random

from numpy.ma.core import append
from pkg_resources import non_empty_lines


### Begin Dr. Forsyth Code. Do Not Modify ###

# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# set the maximum length of the list
max_length = 100

# set the maximum upper bound for the list
upper_bound = 1000

# generate a random lists of integers
nums = generate_random_int_list(max_length, upper_bound)

# create two variables to hold the final answers
num_evens = 0
num_odds = 0

### YOUR CODE BEGINS HERE ###

even_list = list()
odd_list = list ()

for num in nums:
   if num %2 == 0:                  ##Divide number by 2 and only look at the remainder and if that reminder
    even_list.append(num)           ## is 0 (there is no remainder) then it is an even number
    num_evens = even_list
    print (num_evens)
   else:
    odd_list.append(num)
    num_odds = odd_list
    print (num_odds)

print ("This count is even", num_evens)
len1 = len(even_list)                       ##"len"counts the number of entries in a list
print (len1)
print ("The number of entries in even_list is", len1)
num_evens = len1
print (num_evens)

print ("This count is odd", num_odds)
len2 = len(odd_list)
print(len2)
print ("The number of entries in odd_list is", len2)
num_odds = len2
print (num_odds)