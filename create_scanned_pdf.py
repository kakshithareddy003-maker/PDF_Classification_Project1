import pymupdf
from PIL import Image, ImageDraw

# Create a page of text as an image
image = Image.new("RGB", (1000, 700), "white")
draw = ImageDraw.Draw(image)

lines = [
    "INVOICE",
    "ABC SUPPLIES",
    "Invoice Number: INV-101",
    "Date: 12 October 2026",
    "Amount Due: 2500",
    "Payment due within 30 days"
]

y = 100
for line in lines:
    draw.text((100, y), line, fill="black")
    y += 70

# Save image as a PDF page
image.save("scanned_test.pdf", "PDF", resolution=150)

print("Created scanned_test.pdf successfully!")