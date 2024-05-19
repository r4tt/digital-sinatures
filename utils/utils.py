from sage.all import is_prime, is_square, power_mod, fundamental_discriminant, log, floor
    
def is_valid_curve(q,t,r,k,D):
    if q == 0 or t == 0 or r == 0 or k == 0 or D == 0:
        return False
    if not is_prime(q):
        return False 
    if not is_prime(r):
        return False
    if not fundamental_discriminant(D) == D:
        return False
    if D % 4 == 0: #check CM equation
        if not is_square(4*(t*t - 4*q)//D):
            return False
    if D % 4 == 1:
        if not is_square((t*t - 4*q)//D):
            return False
    if not (q+1-t) % r == 0: #check r | #E(F_q)
        return False
    if not power_mod(q,k,r) == 1: #check embedding degree is k
        return False
    return True

def filter_decorator(f):
    def helper(*args):
        q,t,r,k,D = f(*args)
        num_bits = _number_of_bits(r)
        while not is_suitable_curve(q,t,r,k,D, num_bits):
            q,t,r,k,D = f(*args)
            num_bits = _number_of_bits(r)
        return q,t,r,k,D
    return helper
    
def _number_of_bits(n):
    if n == 0:
        return 1
    else:
        return floor(log(n).n()/log(2).n()) + 1

def is_suitable_curve(q,t,r,k,D, num_bits):
    return _number_of_bits(r) >= num_bits and is_valid_curve(q,t,r,k,D)

def is_suitable_q(q):
    return is_prime(q)

def is_suitable_r(r):
    return is_prime(r)
    
    
def print_curve(q,t,r,k,D):
    print(curve_to_string(q,t,k,r,D))
    
def curve_to_string(q,t,k,r,D):
    if q == 0 or t == 0 or r == 0 or k == 0 or D == 0:
        return 'Failed to find an elliptic curve'
    else:
        return 'Elliptic curve over a field of size ' + str(q) + ' with trace ' + str(t) + ', a subgroup of order ' + str(r) + ' with embedding degree ' + str(k) + ', and fundamental discriminant ' + str(D)
    
    
    