# Agentic Web Scraper CLI

โปรแกรมสกัดข้อมูลเว็บระดับสูง (Advanced Web Scraper) พัฒนาด้วย Python และ **Selenium WebDriver** รองรับการดึงข้อมูลจากเว็บไซต์ที่เป็น Dynamic Content (JavaScript Rendered) โดยควบคุมการทำงานผ่านไฟล์ตั้งค่า JSON (Config-Driven Architecture) เสมือนเป็น Agent อัตโนมัติ

---

## คุณสมบัติเด่น (Key Features)

* **Dynamic Scraping**: ใช้ Selenium เพื่อจัดการกับเว็บไซต์ที่โหลดเนื้อหาด้วย JavaScript[cite: 2]
* **Automated WebDriver Management**: จัดการดาวน์โหลดและอัปเดต Browser Driver (Chrome/Firefox) อัตโนมัติด้วย `webdriver-manager`[cite: 2]
* **Config-Driven Automation**: กำหนดกฎการสกัดข้อมูล (URL, Selectors, Pagination) ผ่านไฟล์ `configs/*.json` โดยไม่ต้องแก้ไขโค้ด[cite: 2]
* **Robustness & Error Handling**: มีระบบรอ Element แบบ Explicit Wait, การกดปุ่มซ้ำแบบยืดหยุ่น (Robust Click) และการดักจับ Exception[cite: 2]
* **Structured Output**: แปลงข้อมูลเข้าสู่ Dataclass และส่งออกเป็นไฟล์ `data/scraped_products.json` อัตโนมัติ[cite: 2]

---

## โครงสร้างโปรเจกต์ (Project Structure)

```text
agentic-web-scraper/
├── configs/
│   └── example_site_config.json  # ไฟล์กำหนดกฎและ selectors ในการสแครป
├── data/
│   └── scraped_products.json     # ผลลัพธ์ข้อมูลที่สแครปได้
├── docs/
│   └── ETHICS.md                 # เอกสารแนวทางจริยธรรมและกฎหมาย
├── src/
│   ├── __init__.py               # เครื่องหมายระบุว่าเป็น Python Package
│   ├── config_parser.py          # ตรวจสอบและโหลดไฟล์ JSON Config
│   ├── data_models.py            # Dataclass สำหรับโครงสร้างข้อมูล Product
│   ├── driver_manager.py         # ตัวจัดการเปิด/ปิด Selenium Browser
│   ├── scraper_agent.py          # ตรรกะหลักของ Agent ในการท่องเว็บและดึงข้อมูล
│   └── utils.py                  # ฟังก์ชั่นช่วยเหลือ (Wait, Click, Save JSON)
├── .gitignore                    # ไฟล์และโฟลเดอร์ที่ไม่ติดตามใน Git
├── main.py                       # จุดเริ่มต้นรันโปรแกรม
├── README.md                     # เอกสารอธิบายการใช้งานโปรเจกต์
└── requirements.txt              # ไลบรารีที่จำเป็น (selenium, webdriver-manager ฯลฯ)
```[cite: 2]

---

## การติดตั้งและรันโปรแกรมผ่าน CMD

1. **เปิด CMD แล้วไปยังโฟลเดอร์โปรเจกต์**:
   ```cmd
   cd agentic-web-scraper
   ```[cite: 2]

2. **เปิดใช้งาน Virtual Environment**:
   ```cmd
   venv\Scripts\activate
   ```[cite: 2]

3. **ติดตั้ง Dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```[cite: 2]

4. **สั่งรันโปรแกรม**:
   ```cmd
   python main.py
   ```[cite: 2]

---

## เจาะลึกการทำงานของฟังก์ชั่น (Module Breakdown)

### 1. `src/driver_manager.py` (จัดการ Browser)
* **`get_driver()`**: สร้าง Instance ของ Selenium WebDriver (รองรับ Chrome และ Firefox) พร้อมตั้งค่า Headless mode และ User-Agent[cite: 2]
* **`quit_driver()`**: ปิดการทำงานของ Browser ป้องกัน Context ค้างในระบบ[cite: 2]

### 2. `src/config_parser.py` (อ่านไฟล์ตั้งค่า)
* **`load_config()`**: โหลดไฟล์ JSON จาก `configs/`[cite: 2]
* **`_validate_config()`**: ตรวจสอบความถูกต้องของคีย์ที่จำเป็น เช่น `start_url`, `item_container_selector`, และ `item_data_selectors`[cite: 2]

### 3. `src/data_models.py` (โครงสร้างข้อมูล)
* **`Product`**: `@dataclass` กำหนดโครงสร้างข้อมูลสินค้า (`name`, `price`, `description`, `url`, `image_url`) พร้อมเมธอด `to_dict()` สำหรับแปลงข้อมูลส่งออก[cite: 2]

### 4. `src/utils.py` (เครื่องมือช่วยเหลือ)
* **`wait_for_element()`**: ใช้ `WebDriverWait` รอให้ Element ปรากฏบนหน้าเว็บก่อนดึงข้อมูล[cite: 2]
* **`robust_click()`**: ลองกดปุ่มซ้ำกรณีปุ่มยังไม่พร้อมใช้งาน[cite: 2]
* **`save_data_to_json()`**: บันทึกข้อมูลลิสต์ลงในไฟล์ JSON พร้อมจัดรูปแบบสวยงาม (`indent=4`)[cite: 2]

### 5. `src/scraper_agent.py` (ตรรกะ Agent หลัก)
* **`scrape_page()`**: ค้นหา Element ของสินค้าตาม CSS/XPATH selector ที่ระบุใน config แล้วแปลงเป็นวัตถุ `Product`[cite: 2]
* **`run()`**: ควบคุมลูปการทำงานหลัก เปิด URL เป้าหมาย -> สแครปหน้าปัจจุบัน -> กดปุ่ม Next Page เพื่อไปยังหน้าถัดไป -> เซฟข้อมูล[cite: 2]

### 6. `main.py` (Entry Point)
* อ่าน config จาก `configs/example_site_config.json`[cite: 2]
* เรียกใช้ `ScraperAgent` เพื่อเริ่มกระบวนการสแครปข้อมูลโดยอัตโนมัติ[cite: 2]

---

## จริยธรรมในการดึงข้อมูล (Ethics & Legality)

* **`robots.txt`**: ตรวจสอบสิทธิ์การสแกนของเว็บไซต์เป้าหมายเสมอ[cite: 2]
* **Rate Limiting**: กำหนด `delay_between_pages` ใน Config เพื่อไม่ให้ส่งคำขอถี่เกินไปจนกระทบ Server[cite: 2]
* **Educational Purpose**: โครงสร้างนี้จัดทำขึ้นเพื่อการศึกษาเท่านั้น[cite: 2]