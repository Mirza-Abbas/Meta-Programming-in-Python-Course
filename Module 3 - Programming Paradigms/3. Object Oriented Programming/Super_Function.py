class P: #Parent Class
    def __init__(self):
        print("Parent Class")

class C(P): #Child Class
    def __init__(self):
        super().__init__()
        print("Child Class")

p = P() #Parent Class Instance
c = C() #Child Class Instance