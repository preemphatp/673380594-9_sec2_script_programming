
# สำหรับแต่ละ snippet: โค้ดต้นฉบับมีบั๊ก

print("=" * 50)
print("Snippet A: Infinite Loop ที่แก้แล้ว")
print("=" * 50)
# --- โค้ดต้นฉบับ ---
# counter = 0
# while counter < 5:
#     print(counter)
#     # Missing counter increment!
#
# บั๊ก คือ ไม่มีการเพิ่มค่า counter ในลูป ทำให้ counter < 5 เป็น True ตลอดไป
#       -> ลูปนี้จะวนไม่สิ้นสุด (infinite loop)

# วิธีแก้ คือ ต้องเพิ่มค่า counter ทุกรอบ เช่น counter += 1

counter = 0
while counter < 5:
    print(counter)
    counter += 1  # แก้ไข: เพิ่มค่า counter ทุกรอบ เพื่อให้ลูปจบได้

print()

print("=" * 50)
print("Snippet B: Incorrect Range ที่แก้แล้ว")
print("=" * 50)
# --- โค้ดต้นฉบับ  ---
# for i in range(1, 5):  # Goal: print 1, 2, 3, 4, 5
#     print(i)
#
# บั๊ก คือ: range(1, 5) ให้ค่า 1, 2, 3, 4 เท่านั้น (หยุดก่อนถึง 5 เพราะ stop เป็น exclusive)
#       ทำให้ไม่ได้เลข 5 ตามที่โจทย์ต้องการ
# วิธีแก้: ต้องเปลี่ยนเป็น range(1, 6) เพื่อให้รวมเลข 5 ด้วย

for i in range(1, 6):  # แก้ไข: เปลี่ยน stop จาก 5 เป็น 6
    print(i)

print()

print("=" * 50)
print("Snippet C: Misplaced Break ที่แก้แล้ว")
print("=" * 50)
# --- โค้ดต้นฉบับ  ---
# for char in "hello":
#     if char == 'l':
#         print("Found 'l', stopping!")
#         break
#     print(char)  # This will print 'h', 'e', 'l' then break
#
# วิธีแก้: ย้าย print(char) มาไว้ก่อนเงื่อนไข if เพื่อให้พิมพ์ 'l' ก่อนที่จะ break ออกจากลูป

for char in "hello":
    print(char)  # แก้ไข: พิมพ์ตัวอักษรก่อน จึงได้ h, e, l ครบตามที่ตั้งใจ
    if char == 'l':
        print("Found 'l', stopping!")
        break