list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0

#Outer loop runs 9 times
for i in list1:
    count += 1

    #inner loops runs 9 * 9 = 81 times
    for j in list1:
        count += 1

#81 + 9 = 90
print(count)