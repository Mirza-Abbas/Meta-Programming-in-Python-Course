def calculate_tax (bill, tax_rate):
    return round(bill * tax_rate / 100, 2)

print ("Total:", calculate_tax(225, 15))

print ("Total:", calculate_tax(175, 20))