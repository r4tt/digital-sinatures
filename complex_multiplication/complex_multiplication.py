from sage.all import power_mod, primitive_root, is_square, hilbert_class_polynomial, is_prime,GF, EllipticCurve, kronecker, randint, Integer
from utils import is_valid_curve

def make_curve(q,t,r,k,D):
    assert is_valid_curve(q,t,r,k,D), 'Invalid input. No curve exists.' # check inputs
    print("---AAAAAAA---1----")
    poly = hilbert_class_polynomial(D) # compute hilbert class polynomial
    print("---AAAAAAA---2----")
    j_inv = poly.any_root(GF(q)) # find j-invariant
    print("---AAAAAAA---3----")
    orig_curve = EllipticCurve(GF(q), j=j_inv) # make a curve
    print("---AAAAAAA---4----")
    E = orig_curve
    check = test_curve(q,t,r,k,D,E) # see if this is the right curve
    print("---BBBBBBBBB-------")
    print(check)
    if not check: # not the right curve, use quadratic twist
        E = E.quadratic_twist()
        """
        check = test_curve(q,t,r,k,D,E)
        if not check: # twist didnt work => j = 0 or 1728
            if j_inv == 0: # for j = 0, use sextic twists
                prim = primitive_root(q)
                i = 1
                while t != E.trace_of_frobenius() and i < 6:
                    E = orig_curve.sextic_twist(power_mod(prim,i,q))
                    i+=1
            elif j_inv == 1728: # for j = 1728, use quartic twists
                print("---CCCCCCCC----BEGIN---")
                prim = primitive_root(q)
                print("---CCCCCCCC----END---")
                i = 1
                while t != E.trace_of_frobenius() and i < 4:
                    E = orig_curve.quartic_twist(power_mod(prim,i,q))
                    i+=1
            else:
                return False
            check = test_curve(q,t,r,k,D,E)
    print("---AAAAAAA---5----")
    if not check:
        return False
    """

    return E

def test_curve(q,t,r,k,D,E):
    bool = True
    bool = bool and (power_mod(q, k, r) == 1) #q^k -1 ==0 mod r
    bool = bool and (E.trace_of_frobenius() == t)
    bool = bool and (kronecker((t*t-4*q) * Integer(D).inverse_mod(q),q) == 1)
    bool = bool and (E.cardinality() == q+1-t)
    bool = bool and (E.cardinality() % r ==0)
    return bool
