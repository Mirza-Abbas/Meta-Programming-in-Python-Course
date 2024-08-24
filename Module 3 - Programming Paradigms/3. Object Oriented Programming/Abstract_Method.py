from abc import ABC, abstractmethod #import abstract

class AbsCls (ABC): #Abstract Class
    @abstractmethod
    def absmethod(self):
        pass

class DerivedCls (ABC): #Derived Class
    def absmethod(self):
        print("This is a method called from Derived Class.")

#Creating object of Derived class
obj = DerivedCls()

print(obj.absmethod())
