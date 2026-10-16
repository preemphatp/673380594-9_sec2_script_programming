
# กิจกรรม 2.2: เกมเกมตามหาพลังลึกลับในตำนาน

name = input("กรุณากรอกชื่อผู้เล่น: ").strip()

print(f"\nยินดีต้อนรับ {name} สู่การผจญภัยตามหาพลังในตำนาน!")
print("คุณมาถึงทางแยก 3 ทาง เลือกเส้นทางที่จะเดินทาง:")
print("1. ป่าทึบ")
print("2. ถ้ำหิน")
print("3. แม่น้ำเชี่ยว")
path = input("เลือกเส้นทาง (1/2/3): ").strip()

# กำหนดโจทย์เลขของแต่ละเส้นทาง (ด่าน 1 = ยาก, ด่าน 2 = ง่าย)
if path == "1":
    path_name = "ป่าทึบ"
    stage1_q, stage1_a = "15 + 7 = ", 22
    stage2_q, stage2_a = "12 x 8 = ", 96
elif path == "2":
    path_name = "ถ้ำหิน"
    stage1_q, stage1_a = "20 - 8 = ", 12         
    stage2_q, stage2_a = "144 / 12 = ", 12            
elif path == "3":
    path_name = "แม่น้ำเชี่ยว"
    stage1_q, stage1_a = "18 + 25 = ", 43
    stage2_q, stage2_a = "9 x 7 = ", 63
else:
    print("ตัวเลือกไม่ถูกต้อง กรุณาเริ่มเกมใหม่")
    exit()

print(f"\nคุณเลือกเดินทางสาย {path_name}")

# ด่านที่ 1
print(f"\n--- ด่านที่ 1 ---")
answer1 = input(f"โจทย์: {stage1_q} ")
if not answer1.strip().lstrip("-").isdigit() or int(answer1) != stage1_a:
    print(f"\nผิด! คำตอบที่ถูกคือ {stage1_a}")
    print(f"{name} คุณตอบผิด คุณตรายยย... เกมโอเวอร์")
    exit()

print("ถูกต้อง ผ่านด่านที่ 1")

# ด่านที่ 2
print(f"\n--- ด่านที่ 2 ---")
answer2 = input(f"โจทย์: {stage2_q} ")
if not answer2.strip().lstrip("-").isdigit() or int(answer2) != stage2_a:
    print(f"\nผิด! คำตอบที่ถูกคือ {stage2_a}")
    print(f"{name} คุณตอบผิด คุณตรายยย... เกมโอเวอร์")
    exit()

print("ถูกต้อง ผ่านด่านที่ 2")

# ถึงจุดหมาย - เลือกหีบ
print(f"\n{name} เดินทางผ่านสาย {path_name} มาถึงจุดหมายในที่สุด")
print("ตรงหน้าคุณมีหีบลึกลับ 3 ใบ:")
print("1. หีบสีม่วง")
print("2. หีบสีดำ")
print("3. หีบสีแดง")
chest = input("เลือกเปิดหีบ (1/2/3): ").strip()

if chest == "1":
    power = "เกย์เปิดเผย"
elif chest == "2":
    power = "เกย์ลึกลับ"
elif chest == "3":
    power = "เกย์กึง"
else:
    print("ตัวเลือกไม่ถูกต้อง กรุณาเริ่มเกมใหม่")
    exit()

print(f"\nยินดีด้วย {name} คุณได้รับพลัง {power}")