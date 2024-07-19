#defined by using ** symbols
def total_bill(**a):
    sum = 0
    for x in a.values():
        sum += x
    return round(sum,2)

print(total_bill(coffee = 2.99,
                 cake = 4.55,
                 tax = 0.99))