#functional approach for code re-usability

def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def substraction(num1, num2):
    return num1 - num2


def division(num1, num2):
    return num1 / num2

#Taking inputs from the user

operation= int(input("select operation-\n" \
                 "1. add\n"\
                 "2.multiply\n"\
                 "3.substraction\n"\
                 "4.division\n"\
                 "please select operations from 1, 2, 3, 4 :"))
number1=int(input("Enter First Number "))
number2=int(input("Enter Second Number "))

#conditional statements for which function should call according operation 
if operation == 1:
    print(add(number1, number2))
    
elif operation == 2:
    print(multiply(number1, number2))

elif operation == 3:
    print(substraction(number1, number2))

elif operation == 4:
    print(division(number1, number2))

else :
    print("invalid Operation")
