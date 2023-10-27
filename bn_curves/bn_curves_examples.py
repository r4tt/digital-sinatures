import bn_curves as bn
from utils import print_curve

# Example
num_bits = 160 # number of bits in r
num_curves = 10 # number of curves to find
curves = bn.make_curve(num_bits, num_curves)
for q,t,r,k,D in curves:
    print_curve(q,t,r,k,D)