import My_utils
import math
import random


print("====================================")
My_utils.greet("Preemphat")
print("====================================")

print("\n--- test is_prime() ---")
test_numbers = [1,3,4,5,11,13,17,19,23,29,30,37,42,43,47,53,59,62,67,71,73,80,83,89,97]
for n in test_numbers:
    print(f"{n} เป็นจำนวนเฉพาะหรือไม่: {My_utils.is_prime(n)}")


print("\n--- test math.sqrt() ---")
number_for_sqrt = 64
print(f"รากที่สองของ {number_for_sqrt} คือ {math.sqrt(number_for_sqrt)}")

# --- ใช้ฟังก์ชันจาก standard library: random ---
print("\n--- test random.randint() ---")
random_number = random.randint(1, 100)
print(f"สุ่มตัวเลขระหว่าง 1-100 : {random_number}")