import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from scraper import SimpleWebScraper

def main():
    target_url = "https://automatetheboringstuff.com/2e/"
    scraper = SimpleWebScraper(target_url)
    data = scraper.scrape_main_titles()

    if data:
        print(f"\nBook Title: {data['book_title']}\n")
        print("Chapters:")
        for i, title in enumerate(data['chapter_titles'], 1):
            print(f"{i}. {title}")
    else:
        print("Failed to scrape data.")

if __name__ == "__main__":
    main()