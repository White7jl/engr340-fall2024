import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    a = 1
    b = 1 / math.sqrt(2)
    t = 0.25
    p = 1
    my_pi0 = 0

    for i in range(1,10):
        a1 = (a + b) / 2
        b1 = math.sqrt(a * b)
        p1 = 2 * p
        t1 = (t - p * (a1 - a) ** 2)

        my_pi1 = ((a + b) ** 2) / (4 * t)

        a = a1
        b = b1
        t = t1
        p = p1

        my_pi0 = my_pi1

    # change this so an actual value is returned
    return my_pi0

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
