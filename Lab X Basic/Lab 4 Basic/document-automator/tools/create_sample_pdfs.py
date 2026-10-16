# Creates sample input PDFs for the document automator (coffee shop theme).
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

DOCS = os.path.join(os.path.dirname(__file__), "..", "documents")


def write_pdf(path, pages):
    c = canvas.Canvas(path, pagesize=A4)
    for lines in pages:
        y = 800
        for i, line in enumerate(lines):
            c.setFont("Helvetica-Bold" if i == 0 else "Helvetica", 16 if i == 0 else 12)
            c.drawString(60, y, line)
            y -= 28 if i == 0 else 20
        c.showPage()
    c.save()
    print(f"Created {path}")


os.makedirs(DOCS, exist_ok=True)
write_pdf(os.path.join(DOCS, "input_article.pdf"), [
    ["Coffee Shop Monthly Report",
     "This report summarizes sales and operations for October.",
     "Total orders increased by 12% compared to last month.",
     "Iced Latte and Thai Tea remain the best-selling drinks.",
     "Weekend mornings are the busiest time of the week."],
    ["Inventory and Next Steps",
     "Coffee beans were restocked from 12 kg to 20 kg.",
     "Matcha powder stock was raised to 10 kg for the new menu.",
     "Caramel Syrup was added as a new ingredient.",
     "Next month: launch a seasonal pumpkin latte."],
])
write_pdf(os.path.join(DOCS, "menu_drinks.pdf"), [
    ["Drinks Menu",
     "Iced Latte ........ 65 THB",
     "Espresso .......... 50 THB",
     "Matcha Latte ...... 75 THB",
     "Thai Tea .......... 50 THB"],
])
write_pdf(os.path.join(DOCS, "menu_bakery.pdf"), [
    ["Bakery Menu",
     "Croissant ......... 45 THB",
     "Brownie ........... 40 THB"],
])
