# Activity 2.1: Trace Execution of Conditional Code Snippets

---

## Snippet A

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Grade: {grade}") # What's the output?
```

**Trace:**
| บรรทัด | เงื่อนไข | ผล |
|---|---|---|
| `score = 85` | — | กำหนดค่า `score` เป็น 85 |
| `if score >= 90:` | `85 >= 90` | `False` → ข้าม |
| `elif score >= 80:` | `85 >= 80` | `True` → เข้าบล็อกนี้ กำหนด `grade = "B"` |
| `else:` | — | ไม่ถูกเช็ค เพราะ `elif` ด้านบนเป็นจริง |

**ผลลัพธ์:** `Grade: B`

**เหตุผล:** `if-elif-else` จะหยุดทันทีที่เจอเงื่อนไขแรกที่เป็นจริง จึงไม่ไปเช็คเงื่อนไขที่เหลือต่อ

---

## Snippet B

```python
temp = 25
is_raining = True
if temp > 20 and not is_raining:
    print("Perfect day for a picnic!")
elif temp <= 20 or is_raining:
    print("Stay indoors or bring an umbrella.")
else:
    print("Unsure about the weather.")
# What's the output?
```

**Trace:**
| บรรทัด | เงื่อนไข | ผล |
|---|---|---|
| `temp = 25`, `is_raining = True` | — | กำหนดค่าตัวแปร |
| `if temp > 20 and not is_raining:` | `(25 > 20)` = `True`, `not True` = `False` | `True and False` = `False` → ข้าม |
| `elif temp <= 20 or is_raining:` | `(25 <= 20)` = `False`, `is_raining` = `True` | `False or True` = `True` → เข้าเงื่อนไขนี้ |

**ผลลัพธ์:** `Stay indoors or bring an umbrella.`

**เหตุผล:** เงื่อนไขแรกเป็นเท็จเพราะฝนกำลังตก (`not is_raining` เป็น False) ทำให้ `and` ทั้งก้อนเป็น False จึงไปเช็ค `elif` ซึ่งเป็นจริงเพราะ `is_raining` เป็น True (แค่ตัวเดียวก็พอสำหรับ `or`)

---

## Snippet C

```python
age = 17
has_license = True
if age >= 18:
    if has_license:
        print("You can drive legally.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")
# What's the output?
```

**Trace:**
| บรรทัด | เงื่อนไข | ผล |
|---|---|---|
| `age = 17`, `has_license = True` | — | กำหนดค่าตัวแปร |
| `if age >= 18:` | `17 >= 18` | `False` → ไม่เข้าบล็อกนี้เลย (ข้าม if ชั้นในทั้งหมด) |
| `else:` | — | เข้าเงื่อนไขนี้แทน |

**ผลลัพธ์:** `You are too young to drive.`

**เหตุผล:** เงื่อนไขชั้นนอก (`age >= 18`) เป็นเท็จ โปรแกรมจึงกระโดดไปที่ `else` ทันที โดยไม่เช็ค `has_license` เลย

---

## สรุปแนวคิดสำคัญที่ activity นี้ฝึก

- **`if-elif-else`** หยุดที่เงื่อนไขแรกที่เป็นจริง ไม่เช็คต่อ
- **`and`** ต้องการให้ทุกเงื่อนไขเป็นจริงทั้งหมด, **`or`** ต้องการแค่เงื่อนไขเดียวเป็นจริงก็พอ
- **Nested if** — ถ้าเงื่อนไขชั้นนอกเป็นเท็จ โค้ดชั้นในจะไม่ถูกรันเลย ไม่ว่าเงื่อนไขชั้นในจะเป็นอะไรก็ตาม