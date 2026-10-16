# =================================================================================
# Activity 4.2: Interactive To-Do List (using List Operations)
# สิ่งที่อยากให้ทำ : ให้นักเรียนพัฒนาโปรแกรมจัดการรายการสิ่งที่ต้องทำ (To-Do List) แบบข้อความ (Text-based) อย่างง่าย โดยประยุกต์ใช้ความรู้เรื่องการจัดการ List ที่ได้เรียนมา
# สิ่งที่ต้องมี
# 1. สร้าง List ว่างเริ่มต้นไว้ตัวหนึ่ง ชื่อว่า todo_list
# 2. ใช้การวนลูป while เพื่อแสดงเมนูคำสั่งให้ผู้ใช้เลือก ดังนี้:
# 2.1 เพิ่มรายการงาน (Add a task)
# 2.2 ดูรายการงานทั้งหมด (View tasks)
# 2.3 ทำเครื่องหมายว่างานเสร็จสิ้นแล้ว (ลบงานออก โดยเลือกจากตำแหน่ง Index หรือตามชื่อคำสั่ง)
# 2.4 ออกจากโปรแกรม (Exit)
# 3. ใช้คำสั่ง input() เพื่อรับค่าเมนูที่ผู้ใช้เลือก
# 4. ใช้คำสั่งจัดการ List ต่างๆ (เช่น append(), remove() หรือ pop(), len()) ในการบริหารจัดการข้อมูลใน todo_list
# =================================================================================

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. เพิ่มรายการงาน (Add a task)")
    print("2. ดูรายการงานทั้งหมด (View tasks)")
    print("3. ทำเครื่องหมายว่างานเสร็จสิ้น (Mark task as complete)")
    print("4. ออกจากโปรแกรม (Exit)")


def view_tasks(todo_list):
    if not todo_list:
        print("ยังไม่มีรายการงาน")
        return
    print("รายการงานทั้งหมด:")
    for i, task in enumerate(todo_list):
        print(f"  [{i}] {task}")


def main():
    todo_list = []
    while True:
        show_menu()
        choice = input("เลือกเมนู (1-4): ")

        if choice == "1":
            task = input("กรอกชื่องานที่ต้องการเพิ่ม: ")
            todo_list.append(task)
            print(f"เพิ่ม '{task}' เรียบร้อยแล้ว")

        elif choice == "2":
            view_tasks(todo_list)

        elif choice == "3":
            view_tasks(todo_list)
            if todo_list:
                try:
                    index = int(input("กรอกหมายเลข [index] ของงานที่เสร็จแล้ว: "))
                    completed_task = todo_list.pop(index)
                    print(f"งาน '{completed_task}' เสร็จสิ้นแล้ว และถูกลบออกจากรายการ")
                except (ValueError, IndexError):
                    print("หมายเลขไม่ถูกต้อง กรุณาลองใหม่")

        elif choice == "4":
            print(f"จำนวนงานคงเหลือ: {len(todo_list)} รายการ")
            print("ออกจากโปรแกรม...")
            break

        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง (1-4)")


if __name__ == "__main__":
    main()