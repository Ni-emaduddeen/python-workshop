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