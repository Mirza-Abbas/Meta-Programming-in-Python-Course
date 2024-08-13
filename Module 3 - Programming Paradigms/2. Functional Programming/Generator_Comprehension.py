data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x-1 for x in data if x > 5)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")