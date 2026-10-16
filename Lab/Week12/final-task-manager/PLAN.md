# PLAN: Enhanced Task Manager CLI (Lab 12)

## 1. เป้าหมาย

ต่อยอด Task Manager จาก Class Activity 1 (procedural) และ Class Activity 2 (OOP) ให้เป็นแอป CLI ที่สมบูรณ์ ใช้จัดการงานเรียนของตัวเอง เช่น กำหนดส่ง Lab, วันสอบ, งานที่ยังค้าง

## 2. ฟีเจอร์

| ฟีเจอร์ | รายละเอียด |
|---|---|
| ประเภทงาน 3 แบบ | `Task` งานทั่วไป, `DueDateTask` มีวันกำหนดส่ง, `PriorityTask` มีระดับความสำคัญ High/Medium/Low |
| Tags | ใส่ได้หลายแท็กต่องาน แปลงเป็นตัวพิมพ์เล็กและกันแท็กซ้ำ |
| CRUD | เพิ่ม, ดูทั้งหมด, ทำเครื่องหมายเสร็จ, ลบ |
| Search | ค้นหาคำบางส่วนใน description และ tags ไม่สนตัวพิมพ์เล็ก-ใหญ่ |
| Filter | กรองหลายเงื่อนไขพร้อมกัน: สถานะ, วันส่งก่อน/หลัง, ความสำคัญ, tags |
| Sort | เรียงตาม ID, ชื่อ, สถานะ, วันส่ง, ความสำคัญ ได้ทั้งน้อยไปมากและมากไปน้อย |
| บันทึกข้อมูล | เก็บใน `data/tasks.json` โหลดกลับเป็น object ตามประเภทจริงจากฟิลด์ `_type` |

## 3. โครงสร้าง

```
Task ──┬── DueDateTask   (+ due_date)
       └── PriorityTask  (+ priority)
```

| โมดูล | หน้าที่ |
|---|---|
| `src/task.py` | คลาส Task และคลาสลูก |
| `src/data_persistence.py` | อ่าน/เขียน JSON และแปลงกลับเป็น object |
| `src/task_manager.py` | business logic: เพิ่ม/ลบ/ค้นหา/กรอง/เรียง |
| `src/cli_interface.py` | เมนูและรับ input จากผู้ใช้ |
| `main.py` | จุดเริ่มโปรแกรม |

แยกตามหน้าที่ ถ้าวันหนึ่งจะเปลี่ยนจาก CLI เป็นหน้าเว็บ แก้แค่ `cli_interface.py` ส่วนอื่นใช้ต่อได้

## 4. การทดสอบ

- `python -m unittest discover tests` ผ่าน 8 ข้อ
- ทดสอบเองผ่านเมนู: เพิ่มงานทั้ง 3 แบบ, ใส่วันที่ผิดรูปแบบ, ใส่ priority ที่ไม่มี, ใส่ ID เป็นตัวอักษร โปรแกรมไม่ crash

## 5. Technical Challenges & Solutions

**1. กรองตามวันส่ง ทั้งที่งานบางประเภทไม่มีวันส่ง**
`Task` และ `PriorityTask` ไม่มี `due_date` ถ้าเปรียบเทียบวันที่ตรงๆ จะเกิด `AttributeError` แก้โดยเช็ค `isinstance(t, DueDateTask)` ก่อนเปรียบเทียบ และแปลง input เป็น `datetime.date` ก่อนเทียบ ไม่เทียบเป็น string

**2. เรียงลำดับงานหลายประเภทในรายการเดียว (Polymorphic Sort)**
- เรียงตามวันส่ง: ใช้ key `(t.due_date if isinstance(t, DueDateTask) else datetime.date.max, t.id)` งานที่ไม่มีวันส่งจะได้ค่าวันที่สูงสุด เลยไปอยู่ท้ายรายการเอง
- เรียงตามความสำคัญ: `High`, `Medium`, `Low` เป็น string ถ้าเรียงตรงๆ จะได้ตามตัวอักษร (High, Low, Medium) ซึ่งผิด แก้ด้วย `PRIORITY_MAP = {"High": 1, "Medium": 2, "Low": 3}` แล้วให้งานที่ไม่มี priority เป็น 99

**3. กรองตาม tags หลายตัว**
ต้องการงานที่มีแท็ก **ครบทุกตัว** ที่ระบุ ใช้ `all(tag in t.tags for tag in contains_tags)` ส่วนการค้นหาใช้ `any(...)` เพราะขอแค่เจอในแท็กใดแท็กหนึ่ง

**4. แท็กซ้ำและตัวพิมพ์ไม่เหมือนกัน**
ผู้ใช้พิมพ์ `Study`, ` study ` และ `STUDY` ต้องนับเป็นแท็กเดียวกัน แก้ใน `add_tag()` ด้วย `tag.strip().lower()` และเช็คก่อนเพิ่มว่ามีอยู่แล้วหรือยัง

**5. โหลดกลับเป็น object ตามประเภทเดิม**
JSON เก็บได้แค่ dict ถ้าไม่บอกประเภท จะโหลดกลับมาเป็น `Task` ทั้งหมด แก้โดยให้ `to_dict()` ใส่ฟิลด์ `_type` แล้ว `load_tasks()` อ่าน `_type` เพื่อสร้าง `DueDateTask` หรือ `PriorityTask` ให้ถูก และใส่ `setdefault('tags', [])` ให้อ่านไฟล์เก่าที่ยังไม่มี tags ได้

## 6. Reflection

### ปัญหาที่เจอระหว่างจัดการ repo และส่งงาน

**1. ย้ายโฟลเดอร์ด้วย `git mv` แล้วชื่อเพี้ยน**
ตอนจัด repo เป็น portfolio สั่ง `git mv my-task-manager "Class Activity/Activity 1/"` ทั้งที่ยังไม่ได้สร้างโฟลเดอร์ `Activity 1` Git เลยเปลี่ยนชื่อโฟลเดอร์ `my-task-manager` เป็น `Activity 1` แทนการย้ายเข้าไป แก้โดยเปลี่ยนชื่อกลับ สร้างโฟลเดอร์ปลายทางก่อน แล้วระบุ path ปลายทางเต็ม
→ ได้เรียนรู้ว่าคำสั่งเดียวกันทำงานต่างกันตามสถานะของเครื่อง ต้องเช็คผลด้วย `ls` ทุกครั้งหลังย้ายไฟล์

**2. push ไม่ได้ เพราะเครื่องจำบัญชี GitHub ผิด**
ขึ้น `403 Permission denied to 144P75` เพราะ Windows จำบัญชีที่ใช้กับ Final Project กลุ่ม แก้ด้วยการใส่ username ใน remote URL (`https://preemphatp@github.com/...`) ให้แต่ละ repo ใช้บัญชีของตัวเอง และตั้ง `user.email` ให้ตรงกับประวัติ commit เดิม

**3. ไฟล์ที่ไม่ควรขึ้น GitHub**
- `~$tput_report.docx` ไฟล์ล็อกที่ Word สร้างตอนเปิดไฟล์ค้างไว้ ต้องปิด Word ก่อน `git add` และเพิ่ม `~$*` ใน `.gitignore`
- `.gitignore` ที่เขียน `reports/` กันโฟลเดอร์