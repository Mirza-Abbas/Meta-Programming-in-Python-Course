#Import abc module for ABC(Abstract Base Class)
from abc import ABC

class AbsCls (ABC): #Abstract Class
    pass

class DerivedCls (ABC): #Derived Class
    pass

#Creating object of Derived class
obj = DerivedCls()

print(type(obj))
