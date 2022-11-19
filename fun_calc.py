from function import *

input_num1 = int(input("Enter 1st integer"))
input_num2 = int(input("Enter second integer"))

print("1.Add \n2.Subtract \n3.Multiply \n4.Divide \n5.Remainder")
operator = input("Select: ")

if operator == "1":
    print(add(input_num1, input_num2))
elif operator == "2":
    print(subtract(input_num1, input_num2))
elif operator == "3":
    print(multiply(input_num1, input_num2))
elif operator == "4":
    print(divide(input_num1, input_num2))
elif operator == "5":
    print(find_remainder(input_num1, input_num2))
else:
    print("invalid operator")
