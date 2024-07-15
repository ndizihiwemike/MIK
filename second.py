num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#operators +, -, *, /, %
summed_value = num1 + num2
multiple = num1 * num2
modulus = num2 % num1 
division = num1 / num2
difference = num1 - num2 

print(f"The summed_value is {summed_value}") 
print(f"The multiple is {multiple}") 
print(f"The modulus is {modulus}") 
print(f"The division is {division}") 
print(f"The difference is {difference}")

#conditional statements
if num1 < 10:
    print(f"the first number is lessthan 10")
elif num1 >= 10 and num1 < 50:
    print("fnumber btn 10 and 50")
    if num2 % 2 == 0:
        print("number 2 is even")
    else:
        print("number two is odd")
else:
    print("number is greaterthan or equai to 50")
