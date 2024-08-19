class Payslips:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet."
        
John = Payslips("John", "no", "1000")

Jane = Payslips("Jane", "no", "3000")

print(John.status(), "\n", Jane.status())

John.pay()

print(John.status(), "\n", Jane.status())