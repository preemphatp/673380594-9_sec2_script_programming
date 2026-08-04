# activity5_2.py - Activity 5.2: Word Frequency Counter (using Dictionary)

# 1) รับข้อความประโยคจากผู้ใช้
sentence = input("Enter a sentence: ")

# 2) แปลงข้อความให้เป็นตัวพิมพ์เล็กทั้งหมด
sentence = sentence.lower()

# 3) แยกประโยคออกเป็นคำๆ
words = sentence.split()

# 4) กำหนด Dictionary เปล่าqขึ้นมา
word_counts = {}

# 5-8) วนลูปอ่านคำแต่ละคำ แล้วนับความถี่
for word in words:
    # Challenge: ตัดเครื่องหมายวรรคตอนออกก่อนนับคำ
    clean_word = word.strip('.,!?"')

    if not clean_word:
        continue  # ข้ามคำที่กลาบเป็นค่าว่างหลังตัดเครื่องหมายวรรคตอน

    if clean_word in word_counts:
        word_counts[clean_word] += 1
    else:
        word_counts[clean_word] = 1

# 9) แสดงผลลัพธ์ของ Dictionary word_counts
print("\n--- Word Frequency ---")
for word, count in word_counts.items():
    print(f"{word}: {count}")