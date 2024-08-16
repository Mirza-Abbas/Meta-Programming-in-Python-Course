class Employee:
    Position = ""
    Employeement_Status = ""

    def intro(self):
        return "I am a " + self.Position + " and I am a " + self.Employeement_Status + " employee."
    
emp1 = Employee()

emp1.Position = "Manager"
emp1.Employeement_Status = "Full-Time"

print(emp1.intro())