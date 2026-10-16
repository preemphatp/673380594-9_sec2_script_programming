

def greet(name):
    """พิมพ์ข้อความทักทายไปยังผู้ใช้ตามชื่อที่ระบุ"""
    print(f"Hello, {name}!")


def is_prime(number):
    """ตรวจสอบว่า number เป็นจำนวนเฉพาะ (prime number) หรือไม่
    คืนค่า True ถ้าเป็นจำนวนเฉพาะ, False ถ้าไม่ใช่
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("ตรวจสอบว่า number เป็นจำนวนเฉพาะ (prime number) หรือไม่")