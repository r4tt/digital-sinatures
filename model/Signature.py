class Signature:
    def __init__(self, M, r, s):
        self.M = M
        self.r = r
        self.s = s
    def __str__(self):
        return "M = %s \n r = %s \n s = %d " % (self.M, self.r, self.s)

