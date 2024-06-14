N1 = input("Enter 1st Number: ")
N2 = input("Enter 2nd Number: ")

Sum = float(N1) + float(N2)

#This will through Type Error:
# print("Sum of " + N1 + " and " + N2 + " is: " + Sum)

#Solution:
print("Sum of " + str(N1) + " and " + str(N2) + " is: " + str(Sum))