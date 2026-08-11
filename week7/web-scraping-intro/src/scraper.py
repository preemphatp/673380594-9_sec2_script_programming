import requests
from bs4 import BeautifulSoup

class SimpleWebScraper:
    def __init__(self, target_url):
        self.target_url = target_url

    def _get_html_content(self):
        try:
            # เพิ่ม User-Agent เพื่อป้องกันโดนระบบบล็อก
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(self.target_url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            return None

    def scrape_main_titles(self):
        html = self._get_html_content()
        if not html:
            return None
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # 1. ดึงชื่อหนังสือจาก <h1> หรือ Tag <title>
        h1_tag = soup.find('h1')
        book_title = h1_tag.get_text(strip=True) if h1_tag else (soup.title.get_text(strip=True) if soup.title else "Title Not Found")

        # 2. ดึงชื่อบทเรียนจากแท็ก <a> ที่มีลิงก์ไปยัง chapter หรือมีคำว่า Chapter
        chapter_titles = []
        for link in soup.find_all('a'):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            # คัดกรองเอาเฉพาะลิงก์ที่เป็นบทเรียน
            if ('chapter' in href.lower() or 'chapter' in text.lower()) and text:
                if text not in chapter_titles:
                    chapter_titles.append(text)

        return {"book_title": book_title, "chapter_titles": chapter_titles}