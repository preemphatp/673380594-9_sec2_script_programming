import math

print("--- Lab 4.2: Geometric Calculations ---")

# 1) กำหนดจุดสองจุดด้วย tuple: point1 และ point2
point1 = (3, 4)
point2 = (6, 8)

# 2) เข้าถึงค่าพิกัด x, y ของแต่ละจุด
print("\n[1] Access Coordinates")
print(f"Point 1: x = {point1[0]}, y = {point1[1]}")
print(f"Point 2: x = {point2[0]}, y = {point2[1]}")

# 3) ทดลองแก้ไขค่าใน tuple เพื่อแสดงให้เห็นว่า tuple เปลี่ยนแปลงไม่ได้ (immutable)
print("\n[2] Attempt Modification (Immutability Demonstration)")
try:
    point1[0] = 5  # บรรทัดนี้จะทำให้เกิด TypeError เพราะ tuple แก้ไขไม่ได้
except TypeError as e:
    print(f"Error trying to modify tuple: {e}")

# 4) คำนวณระยะห่างระหว่างจุดสองจุดด้วยสูตรระยะทาง
#    distance = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
print("\n[3] Calculate Distance")
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print(f"Distance between point1 {point1} and point2 {point2}: {distance}")


# ======================================================================

# ให้นักศึกษาลองต่อยอดเอง (Challenge):
# ลองแก้โค้ดให้รับพิกัดของจุดใหม่ 2 จุดจากผู้ใช้ผ่าน input()
# (อย่าลืมแปลงชนิดข้อมูลจาก input() ให้เป็นตัวเลขก่อนนำไปคำนวณ)
# แล้วคำนวณระยะห่างระหว่างจุดทั้งสองที่ผู้ใช้กรอกเข้ามา
# ======================================================================
def calculate_distance_from_input():
    print("\n[Challenge] กรอกพิกัดจุดใหม่ 2 จุด")
    x1 = float(input("Point A - x: "))
    y1 = float(input("Point A - y: "))
    x2 = float(input("Point B - x: "))
    y2 = float(input("Point B - y: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    new_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"Distance between {point_a} and {point_b}: {new_distance}")


if __name__ == "__main__":
    pass
    