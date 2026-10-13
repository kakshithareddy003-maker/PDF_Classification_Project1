import pytesseract
from PIL import Image
from pathlib import Path

# Location of Tesseract OCR on your computer
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Image location
image_path = Path(r"C:\Users\kaksh\Downloads\bill3.png")

# Output text file in your project folder
output_path = Path("bill3_receipt_text.txt")

try:
    if not image_path.exists():
        print("Image not found:", image_path)
    else:
        print("Opening image...")
        image = Image.open(image_path).convert("RGB")

        print("Extracting text using OCR...")
        text = pytesseract.image_to_string(image)

        print("\n========== EXTRACTED TEXT ==========\n")
        print(text)
        print("\n====================================")

        output_path.write_text(text, encoding="utf-8")
        print(f"\nText saved successfully to: {output_path.resolve()}")

except Exception as error:
    print("\nAn error occurred:")
    print(error)