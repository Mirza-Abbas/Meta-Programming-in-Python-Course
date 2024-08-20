class A: #Parent Class
    a = 7

class B(): #Parent Class
    b = 8

class C(A, B): #Child Class
    pass

c = C()

print(c.a, c.b)