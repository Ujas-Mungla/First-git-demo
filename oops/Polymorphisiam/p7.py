class Poly:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

p1 = Poly()
print(p1.add(10, 20))
print(p1.add(10, 20, 30))
