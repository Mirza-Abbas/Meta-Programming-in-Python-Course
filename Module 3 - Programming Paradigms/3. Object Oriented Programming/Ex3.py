#Exercise: Classes and object exploration

class A: #Class definition of A
   
   def __init__(self, c): #Constructor for A
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self): #Definition of local method alpha()
       c = self.c + 1
       return c

print(dir(A)) #Instantiating object a over class A
print("Instantiating A..")
a = A(1)
print(a.alpha()) #Calling method alpha() over object of class A

class B: #Class definition of B
   
   def __init__(self, a): #Constructor for B
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha()) #Calling method alpha() over object of class A 
   d = 5
   print(d)
   print(a)

print("Instantiating B..")

b = B(a) #Instantiating object a over class B *
print(a)