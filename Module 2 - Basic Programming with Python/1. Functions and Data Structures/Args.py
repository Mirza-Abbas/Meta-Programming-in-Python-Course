#defined by using * symbol
def sum_of(*a):
    sum = 0
    for x in a:
        sum += x
    return sum

print(sum_of(1, 2, 3, 4, 5))