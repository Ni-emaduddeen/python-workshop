import random

def calculate(number1, operation, number2):
    # ฟังก์ชันนี้ทำหน้าที่คำนวณอย่างเดียว
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 == 0:
            return "Error: Cannot divide by 0"
        return number1 / number2
    else:
        return "Error: Invalid operation"

def run_calculator():
    # ฟังก์ชันนี้ทำหน้าที่รับค่าและแสดงผล
    print("--- Calculator ---")
    number1 = int(input("enter the first number :"))
    operation = input("Select an operation (+,-,*,/):")
    number2 = int(input("enter the second number :"))
    
    # เรียกใช้ฟังก์ชัน calculate เพื่อหาผลลัพธ์
    result = calculate(number1, operation, number2)
    
    # เช็กว่าผลลัพธ์เป็นข้อความ Error หรือไม่
    if type(result) == str:
        print(result)
    else:
        print(number1, operation, number2, "=", result)

def run_guessing_game():
    print("\n--- Guessing Game ---")
    number = random.randint(0,10)
    guess = int(input("guess a number between 0-10 :"))

    while guess != number:
        # เช็กว่าค่าที่ทายมากไปหรือน้อยไป
        if guess > number:
            print("Too high! try again")
        elif guess < number:
            print("Too low! try again")
            
        guess = int(input("guess a number between 0-10 :"))

    print("Gooddd!!!!!")

# เรียกใช้งานฟังก์ชันเครื่องคิดเลข
run_calculator()

# เรียกใช้งานฟังก์ชันเกมทายเลข
run_guessing_game()
