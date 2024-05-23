from sage.all import power_mod, primitive_root, is_square, hilbert_class_polynomial, is_prime,GF, EllipticCurve, kronecker, randint, Integer
from utils import is_valid_curve

def make_curve(q,t,r,k,D):
    assert is_valid_curve(q,t,r,k,D), 'Invalid input. No curve exists.' # check inputs
    poly = hilbert_class_polynomial(D) # compute hilbert class polynomial
    j_inv = poly.any_root(GF(q)) # find j-invariant
    orig_curve = EllipticCurve(GF(q), j=j_inv) # make a curve
    E = orig_curve
    check = test_curve(q,t,r,k,D,E) # see if this is the right curve
    if not check: # not the right curve, use quadratic twist
        E = E.quadratic_twist()
    return E

def test_curve(q,t,r,k,D,E):
    bool = True
    bool = bool and (power_mod(q, k, r) == 1) #q^k -1 ==0 mod r
    bool = bool and (E.trace_of_frobenius() == t)
    bool = bool and (kronecker((t*t-4*q) * Integer(D).inverse_mod(q),q) == 1)
    bool = bool and (E.cardinality() == q+1-t)
    bool = bool and (E.cardinality() % r ==0)
    return bool
