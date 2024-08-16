class Alpha:
    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’

a1 = Alpha()

#This will throw error:
#print(a1.__b)