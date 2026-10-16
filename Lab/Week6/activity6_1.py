"""
แก้จาก Lab2_1.py ให้เป็นฟังก์ชัน 2 ฟังก์ชัน
"""


def is_positive_negative_zero(num):
   
    if num < 0:
        return f"{num} เป็นจำนวนติดลบ (negative number)"
    elif num > 0:
        return f"{num} เป็นจำนวนบวก (positive number)"
    else:
        return f"{num} เป็นศูนย์ (zero)"

def is_even_odd(num):
   
    if num % 2 == 0:
        return f"{num} เป็นเลขคู่ (even number)"
    else:
        return f"{num} เป็นเลขคี่ (odd number)"


def main():
    print()
    print("=== Number Classifier (Refactored with Functions) ===")
    print("พิมพ์ exit เพื่อออกจากโปรแกรม\n")

    while True:
        user_input = input("ใส่ตัวเลขที่ต้องการ (หรือ exit เพื่อออกจากโปรแกรม): ").strip()

        if user_input.lower() == "exit":
            print("ออกจากโปรแกรม... ขอบคุณฮ๊าพ")
            break

        try:
            num = int(user_input)
        except ValueError:
            print("กรุณาป้อนจำนวนเต็มให้ถูกต้อง\n")
            continue

        print(is_positive_negative_zero(num))
        print(is_even_odd(num))
        print()


if __name__ == "__main__":
    main()