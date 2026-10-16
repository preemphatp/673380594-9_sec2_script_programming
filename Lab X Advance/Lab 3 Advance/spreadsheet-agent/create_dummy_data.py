# create_dummy_data.py
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "SalesData"

ws.append(["Product Name", "Quantity", "Unit Price"])

data = [
    ["Iced Latte", 30, 65.00], ["Espresso", 18, 50.00], ["Matcha Latte", 25, 75.00],
    ["Thai Tea", 40, 50.00], ["Americano", 22, 55.00], ["Cocoa", 12, 60.00],
    ["Caramel Macchiato", 15, 75.00], ["Croissant", 20, 45.00], ["Brownie", 16, 40.00]
]
for row in data:
    ws.append(row)

import os
os.makedirs("data", exist_ok=True)
wb.save("data/input_data.xlsx")
print("✅ สร้างไฟล์ data/input_data.xlsx สำเร็จ!")
