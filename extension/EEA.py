
#y^-1 % x
def eea(y, x):
    n = x
    x_c1, x_c2 = 1, 0
    y_c1, y_c2 = 0, 1
    while True:
        # get quotient and remainder
        q, r = divmod(x, y)
        # if found GCD, return
        if r == 0:
            return (n + y_c2) % n
        # else, keep track
        x_c1, x_c2, y_c1, y_c2 = y_c1, y_c2,  x_c1 - q * y_c1, x_c2 - q * y_c2
        x, y = y, r
