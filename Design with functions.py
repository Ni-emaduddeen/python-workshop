import math
from functools import reduce

# ==========================================
# 1. displayRange recursive function
# ==========================================
def displayRange(lower, upper):
    """ฟังก์ชันพิมพ์ตัวเลขจาก lower ถึง upper แบบ Recursive"""
    # ใช้เงื่อนไข if เพื่อตรวจสอบ Base case ป้องกัน Infinite recursion
    if lower <= upper:
        print(lower)
        # เรียกใช้ตัวเอง (Recursive step) พร้อมขยับค่า lower ขึ้นทีละ 1
        displayRange(lower + 1, upper)

# ==========================================
# 2. summation function with default arguments
# ==========================================
def summation(lower, upper, step=1, func=lambda x: x):
    """ฟังก์ชันหาผลรวม โดยมี Default arguments สำหรับ step และ function"""
    result = 0
    while lower <= upper:
        # นำค่าที่ผ่านฟังก์ชัน (func) มาบวกทบใน running total
        result += func(lower)
        # เลื่อนไปยังตัวเลขถัดไปตามค่า step
        lower += step
    return result

# ==========================================
# 3. ส่วนของการทดสอบและใช้งาน (Main Execution)
# ==========================================
if __name__ == "__main__":
    
    # ------------------------------------------
    # ทดสอบฟังก์ชัน displayRange
    print("--- Testing displayRange(1, 5) ---")
    displayRange(1, 5)
    
    # ------------------------------------------
    # ทดสอบฟังก์ชัน summation 
    print("\n--- Testing summation(1, 100, 2, math.sqrt) ---")
    # หาผลรวมของรากที่สองของตัวเลขตั้งแต่ 1 ถึง 100 โดยกระโดดข้ามทีละ 2
    sum_result = summation(1, 100, 2, math.sqrt)
    print("Result:", sum_result)
    
    # ------------------------------------------
    # ตัวแปรจำลองสำหรับทดสอบ Mapping และ Filtering
    numbers = [-10, -5, 0, 3, 7, -2, 15]
    
    # Mapping: สร้าง list ของค่าสัมบูรณ์ (Absolute values)
    absolute_values = list(map(abs, numbers))
    print("\n--- Mapping (Absolute values) ---")
    print(absolute_values)
    
    # Filtering: สร้าง list ของตัวเลขจำนวนบวก โดยบังคับใช้ lambda
    positive_numbers = list(filter(lambda x: x > 0, numbers))
    print("\n--- Filtering (Positive numbers) ---")
    print(positive_numbers)
    
    # ------------------------------------------
    # ตัวแปรจำลองสำหรับทดสอบ Reducing
    words = ["Python", "Functional", "Programming", "is", "Fun"]
    
    # Reducing: สร้าง single string จาก list ของ strings
    single_string = reduce(lambda x, y: x + " " + y, words)
    print("\n--- Reducing (Single string) ---")
    print(single_string)