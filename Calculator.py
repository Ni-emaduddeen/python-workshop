import random

def calculate(number1, operation, number2):
    try:
        if operation == '+':
            return number1 + number2
        elif operation == '-':
            return number1 - number2
        elif operation == '*':
            return number1 * number2
        elif operation == '/':
            return number1 / number2
        else:
            return "Error: Invalid operation"
    except ZeroDivisionError:
        return "Error: Cannot divide by 0"

def run_calculator():
    print("--- Calculator ---")
    # ใช้ while True เพื่อให้วนลูปรับค่าใหม่ถ้าพิมพ์ผิด
    while True:
        try:
            number1 = int(input("enter the first number :"))
            operation = input("Select an operation (+,-,*,/):")
            number2 = int(input("enter the second number :"))
            
            result = calculate(number1, operation, number2)
            
            if type(result) == str:
                print(result)
            else:
                print(number1, operation, number2, "=", result)
            
            # ถ้าโค้ดทำงานมาถึงตรงนี้แปลว่าไม่มี Error ให้ break เพื่อออกจากลูปเครื่องคิดเลข
            break 
            
        except ValueError:
            print("Error: Please enter numbers only!\n") # ใส่ \n เพื่อเว้นบรรทัดให้ดูง่ายขึ้นตอนเริ่มลูปใหม่

def run_guessing_game():
    print("\n--- Guessing Game ---")
    number = random.randint(0,10)
    
    while True:
        try:
            guess = int(input("guess a number between 0-10 :"))
            
            if guess == number:
                print("Gooddd!!!!!")
                break 
            elif guess > number:
                print("Too high! try again")
            elif guess < number:
                print("Too low! try again")
                
        except ValueError:
            print("Error: Please enter numbers only!")

# เรียกใช้งานฟังก์ชันเครื่องคิดเลข
run_calculator()

# เรียกใช้งานฟังก์ชันเกมทายเลข
run_guessing_game()
