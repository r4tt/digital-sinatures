import random

import cocks_pinch as cp
import complex_multiplication as cm
from utils import print_curve


# # Example 1 (using a known value of r)
# k = 5 # embedding degree
# r = 1743941 # size of prime order subgroup
# r,k,D = cp.gen_params_from_r(r,k) # find a valid D
# q,t,r,k,D = cp.run(r,k,D) # use CP method to solve for q and t
# print_curve(q,t,r,k,D)
#
# # Example 2 (algorithm generates r)
# k = 7 # embedding degree
# num_bits = 100 # number of bits in size of prime order subgroup
# r,k,D = cp.gen_params_from_bits(num_bits,k)
# q,t,r,k,D = cp.run(r,k,D) # use CP method to solve for q and t
# print_curve(q,t,r,k,D)
#
# # Example 3 (running cocks_pinch_method once with a specified num_times and g)
# k = 5
# r = 1743941
# r,k,D = cp.gen_params_from_r(r,k)
# g = 722825
# q,t = cp.method(r,k,D,max_trials=100,g=g) # might not find q and t
# print_curve(q,t,r,k,D)


def create_cv_from_bits(num_bits, k):
    r, k, D = cp.gen_params_from_bits(num_bits, k)
    while (D < -20):
        r, k, D = cp.gen_params_from_bits(num_bits, k)
    q, t, r, k, D = cp.run(r, k, D)
    print_curve(q, t, r, k, D)
    E = cm.make_curve(q, t, r, k, D)
    print(E)
    return E

k = random.randint(3, 10)
num_bits = 256
E = create_cv_from_bits(num_bits, k)

print(E)
