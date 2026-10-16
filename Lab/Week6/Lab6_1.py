import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

def add(a, b):
    """รับตัวเลข a และ b แล้วคืนค่าผลบวก (a + b)"""
    return a + b


def subtract(a, b):
    """รับตัวเลข a และ b แล้วคืนค่าผลลบ (a - b)"""
    return a - b


def multiply(a, b):
    """รับตัวเลข a และ b แล้วคืนค่าผลคูณ (a * b)"""
    return a * b


def divide(a, b):
    """รับตัวเลข a และ b แล้วคืนค่าผลหาร (a / b)
    ถ้า b เป็น 0 จะคืนข้อความแจ้งเตือน แทนที่จะทำให้โปรแกรมพัง
    """
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base, exponent=2):
    """รับ base และ exponent (ค่าเริ่มต้น = 2 คือยกกำลังสอง)
    แล้วคืนค่า base ยกกำลัง exponent
    """
    return base ** exponent


def get_number(prompt):
    """รับค่าตัวเลข (float) จากผู้ใช้ พร้อมตรวจสอบความถูกต้อง"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("กรุณาป้อนตัวเลขให้ถูกต้อง")


def main():
    """เมนูหลักแบบ while loop ให้ผู้ใช้เลือกการดำเนินการ"""
    menu = """
==== เครื่องคิดเลขอย่างง่าย ====
1. บวก 
2. ลบ 
3. คูณ 
4. หาร 
5. ยกกำลัง 
0. ออกจากโปรแกรม (Exit)
=====================================================
"""
    while True:
        print(menu)
        choice = input("เลือกเมนู (0-5): ").strip()

        if choice == "0":
            print("ออกจากโปรแกรม... ขอบคุณที่ใช้บริการ")
            break

        elif choice in ("1", "2", "3", "4"):
            num1 = get_number("ป้อนตัวเลขที่ 1: ")
            num2 = get_number("ป้อนตัวเลขที่ 2: ")

            if choice == "1":
                result = add(num1, num2)
                print(f"ผลลัพธ์: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"ผลลัพธ์: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"ผลลัพธ์: {num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"ผลลัพธ์: {num1} / {num2} = {result}")

        elif choice == "5":
            base = get_number("ป้อนฐาน (base): ")
            exp_input = input("ป้อนเลขยกกำลัง (Enter เพื่อใช้ค่าเริ่มต้น = 2): ").strip()
            if exp_input == "":
                result = power(base)
                print(f"ผลลัพธ์: {base} ** 2 (default) = {result}")
            else:
                exponent = float(exp_input)
                result = power(base, exponent)
                print(f"ผลลัพธ์: {base} ** {exponent} = {result}")

        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง (0-5)")


if __name__ == "__main__":
    main()