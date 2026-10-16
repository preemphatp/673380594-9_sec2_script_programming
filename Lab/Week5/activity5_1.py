# activity5_1.py - Activity 5.1: Real-World Applications of Dictionaries and Sets

discussion = [
    {
        "prompt": "จะนำ Dictionary ไปใช้ตรงไหนในเกมได้บ้าง?",
        "answer": "ใช้เก็บช่องเก็บของผู้เล่น (Inventory) หรือค่าพลังของตัวละคร (Stats) "
                  "เช่น player_inventory = {'sword': 1, 'potion': 3} "
                  "เพราะต้องเข้าถึงข้อมูลตาม key (ชื่อไอเทม/สถานะ) ได้อย่างรวดเร็ว",
    },
    {
        "prompt": "Dictionary จะช่วยจัดเก็บข้อมูลสินค้าในร้านค้าออนไลน์ได้อย่างไร?",
        "answer": "ใช้รหัสสินค้า (Product ID) เป็น key และรายละเอียดสินค้า "
                  "(ชื่อ, ราคา, สต็อก) เป็น value เช่น "
                  "products = {'P001': {'name': 'เสื้อยืด', 'price': 199}} "
                  "ทำให้ค้นหาสินค้าตามรหัสได้เร็วโดยไม่ต้องวนลูปทั้งลิสต์",
    },
    {
        "prompt": "Set จะมีประโยชน์อย่างไรในการจัดการสิทธิ์ของผู้ใช้หรือแท็ก?",
        "answer": "ใช้เก็บบทบาท (roles) หรือแฮชแท็กที่ไม่ซ้ำกัน เช่น "
                  "user_roles = {'admin', 'editor'} เพราะ Set ป้องกันข้อมูลซ้ำ "
                  "และเช็คได้เร็วว่ามีสิทธิ์นั้นอยู่หรือไม่ด้วย in",
    },
    {
        "prompt": "สถานการณ์ไหนที่ต้องเช็กเร็วว่า 'มีข้อมูลนี้อยู่ในกลุ่มข้อมูลขนาดใหญ่หรือไม่' "
                  "โดยไม่สนใจลำดับ?",
        "answer": "เช่น รายชื่อ IP Address ที่ถูกบล็อก (blocked_ips) หรือการนับผู้เข้าชมเว็บ "
                  "ที่ไม่ซ้ำคน (unique_visitors) เพราะ Set ใช้ hashing ทำให้การเช็ค "
                  "'in' เร็วกว่าการวนลูปใน List มาก โดยเฉพาะเมื่อข้อมูลมีจำนวนมาก",
    },
]

print("--- Activity 5.1: Real-World Applications of Dictionaries and Sets ---\n")
for i, item in enumerate(discussion, start=1):
    print(f"{i}. คำถาม: {item['prompt']}")
    print(f"   คำตอบ: {item['answer']}\n")