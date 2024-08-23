class Employees: #Parent Class
    def __init__(self, name, last):
        self.name = name
        self.last = last
    
class Supervisors (Employees): #Child Class
    def __init__(self, name, last, password): #Modifying Method
        super().__init__(name, last) #Used to access & initiate parent variables
        self.password = password

class Chef (Employees): #Child Class
    def leave_request(self, days): #Additional Method
        return "May I take a leave for " + str(days) + " days."
    
John = Supervisors("John",  "Doe", "1234")

print(John.name)
print(John.last)
print(John.password)

Jane = Chef("Jane", "Doe")
print(Jane.leave_request(3))