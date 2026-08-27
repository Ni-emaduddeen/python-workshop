number1 = int(input("enter the first number :"))
operation = input("Select an operation (+,-,*,/):")
number2 = int(input("enter the second number :"))

if operation == '+' :
    result = number1 + number2
elif operation == '-' :
    result = number1 - number2
elif operation == '*' :
    result = number1 * number2
elif operation == '/' :
    result = number1 / number2

print(number1, operation, number2 ,"=", result)
import random

number = random.randint(0,10)
guess = int(input("guess a number between 0-10 :"))

while guess != number :
    print("try again na")
    guess = int(input("guess a number between 0-10 :"))

print("Gooddd!!!!!")
