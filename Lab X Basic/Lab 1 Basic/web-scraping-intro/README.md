# Web Scraping Intro CLI Application

A Python-based command-line interface (CLI) application designed to introduce web scraping fundamentals. The application downloads HTML web pages using the `requests` library and extracts targeted content using `BeautifulSoup4`, scraping the main book title and chapter list from [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/).

---

## Ethical Considerations & Legality

When performing web scraping, adhere to these key ethical rules:
* **Robots.txt**: Always check the site's `robots.txt` rules (e.g., `https://example.com/robots.txt`) before scraping.
* **Rate Limiting**: Avoid overloading web servers with rapid requests; use delays when scraping multiple pages.
* **User-Agent Header**: Include a descriptive `User-Agent` string in request headers to identify your script politely to the server.

---

## Project Directory Structure

```text
web-scraping-intro/
├── data/                  # Directory for storing scraped data outputs
├── src/
│   ├── __init__.py        # Marks 'src' as a Python package
│   └── scraper.py         # Web scraper class and scraping logic
├── .gitignore             # Specifies files ignored by Git (venv, __pycache__)
├── main.py                # Main execution entry point
├── README.md              # Project overview and documentation
└── requirements.txt       # Project dependencies (requests, beautifulsoup4)
```

---

## Installation & Setup (Windows CMD)

1. **Navigate to the project root directory**:
   ```cmd
   cd web-scraping-intro