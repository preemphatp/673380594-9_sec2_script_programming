print("--- Lab 4.1: Student Management System ---")

# 1) เริ่มต้นด้วย list ว่างสำหรับเก็บชื่อนักศึกษา
student_names = []

# 2) เพิ่มนักศึกษา: รับชื่อจากผู้ใช้ 3 คน แล้ว append() เข้า list
print("\n[1] Add Students")
for i in range(3):
    name = input(f"Enter student name #{i + 1}: ")
    student_names.append(name)

print(f"Current list: {student_names}")

# 3) ค้นหานักศึกษา: ใช้ 'in' เพื่อเช็คว่ามีชื่อนี้อยู่ใน list หรือไม่
#    ถ้าพบ ให้แสดง index ด้วย index()
print("\n[2] Find a Student")
search_name = input("Enter a name to search for: ")

if search_name in student_names:
    position = student_names.index(search_name)
    print(f"Found '{search_name}' at index {position}")
else:
    print(f"'{search_name}' not found in the list")

# 4) ลบนักศึกษา: เช็คก่อนว่ามีอยู่จริงหรือไม่ (กัน error) แล้วค่อย remove()
print("\n[3] Remove a Student")
remove_name = input("Enter a name to remove: ")

if remove_name in student_names:
    student_names.remove(remove_name)
    print(f"'{remove_name}' has been removed")
else:
    print(f"'{remove_name}' not found, nothing removed")

print(f"Updated list: {student_names}")

# 5) เรียงลำดับรายชื่อตามตัวอักษรด้วย sort()
print("\n[4] Sort Students")
student_names.sort()
print(f"Sorted list: {student_names}")

# 6) นับจำนวนนักศึกษาทั้งหมดด้วย len()
print("\n[5] Count Students")
print(f"Total students: {len(student_names)}")


# ======================================================================
# Challenge: ระบบเมนูสั่งการแบบง่ายๆ ด้วย while loop
# (เพิ่ม / ลบ / ค้นหา / เรียงลำดับ / นับจำนวน / ออกจากโปรแกรม)
# หมายเหตุ: เขียนแยกเป็นฟังก์ชัน student_menu() ไม่รบกวนโค้ดหลักด้านบน
# ต้องการทดสอบ ให้ uncomment บรรทัด student_menu() ที่ท้ายไฟล์
# ======================================================================
def student_menu():
    names = []  # ใช้ list ใหม่แยกจากด้านบน เพื่อทดสอบระบบเมนูอิสระ

    while True:
        print("\n===== เมนูจัดการรายชื่อนักเรียน =====")
        print("1. เพิ่มนักเรียน (Add)")
        print("2. ค้นหานักเรียน (Search)")
        print("3. ลบนักเรียน (Remove)")
        print("4. เรียงลำดับรายชื่อ (Sort)")
        print("5. นับจำนวนนักเรียน (Count)")
        print("6. แสดงรายชื่อทั้งหมด (Show all)")
        print("7. ออกจากโปรแกรม (Exit)")
        choice = input("เลือกเมนู (1-7): ")

        if choice == "1":
            name = input("กรอกชื่อนักเรียนที่ต้องการเพิ่ม: ")
            names.append(name)
            print(f"รายชื่อปัจจุบัน: {names}")
        elif choice == "2":
            name = input("กรอกชื่อนักเรียนที่ต้องการค้นหา: ")
            if name in names:
                print(f"พบ '{name}' ที่ตำแหน่ง (index) {names.index(name)}")
            else:
                print(f"ไม่พบ '{name}' ในรายชื่อ")
        elif choice == "3":
            name = input("กรอกชื่อนักเรียนที่ต้องการลบ: ")
            if name in names:
                names.remove(name)
                print(f"ลบ '{name}' เรียบร้อยแล้ว")
            else:
                print(f"ไม่พบ '{name}' ในรายชื่อ ไม่สามารถลบได้")
            print(f"รายชื่อปัจจุบัน: {names}")
        elif choice == "4":
            names.sort()
            print(f"รายชื่อหลังเรียงลำดับ: {names}")
        elif choice == "5":
            print(f"จำนวนนักเรียนทั้งหมด: {len(names)} คน")
        elif choice == "6":
            print(f"รายชื่อนักเรียนทั้งหมด: {names}")
        elif choice == "7":
            print("ออกจากโปรแกรม...")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง (1-7)")


if __name__ == "__main__":
   
    pass
    