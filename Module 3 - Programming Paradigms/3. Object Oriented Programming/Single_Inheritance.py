class P: #Parent Class
    def __init__(self):
        self.a = 7

class C(P): #Child Class
    pass

p = P() #Parent Class Instance
c = C() #Child Class Instance

print(p.a)
print(c.a)