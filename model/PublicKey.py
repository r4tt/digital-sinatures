class PublicKey:
    def __init__(self, E, P, n, Q):
        self.E = E
        self.P = P
        self.n = n
        self.Q = Q

    def __str__(self):
        return "E = %s \n P = %s \n n = %d \n Q = %s" % (self.E, self.P, self.n, self.Q)
