#Exercise: Define a Class

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

house = House()
print(house.num_rooms)
print(House.num_rooms)

#Changing attribute of instance object
house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms) #No effect on attribute of class object

#Changing attribute of class object
House.num_rooms = 9
print(house.num_rooms) 
print(House.num_rooms)