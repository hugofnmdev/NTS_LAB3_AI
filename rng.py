class PseudoRNG:
    
    def __init__(self,a,b,val,prime = 2147483647):
        self.prime = prime
        self.a = a
        self.b = b
        self.val = val

    def nextInt(self):
        self.val = (self.val*self.a+self.b) % self.prime
        return self.val
    
    def randInt(self,inf,sup):
        x = self.nextInt()
        return inf + x % (sup-inf)


