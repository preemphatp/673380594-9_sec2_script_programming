# Creates sample input PDFs for the document agent (coffee shop theme).
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
write_pdf(os.path.join(DOCS, "source_document.pdf"), [
    ["Signature Recipe: Caramel Macchiato",
     "Internal document - staff only.",
     "1. Pump 2 shots of caramel syrup into a 16 oz cup.",
     "2. Add 200 ml of steamed fresh milk.",
     "3. Pour 2 shots of espresso slowly over the milk.",
     "4. Finish with a caramel drizzle in a crosshatch pattern."],
])
write_pdf(os.path.join(DOCS, "staff_handbook_part1.pdf"), [
    ["Staff Handbook - Part 1: Opening Shift",
     "Arrive 30 minutes before opening.",
     "Calibrate the espresso grinder and pull a test shot.",
     "Check milk and syrup stock levels."],
])
write_pdf(os.path.join(DOCS, "staff_handbook_part2.pdf"), [
    ["Staff Handbook - Part 2: Closing Shift",
     "Backflush the espresso machine.",
     "Record leftover bakery items in the waste log.",
     "Lock the cash drawer and set the alarm."],
])
