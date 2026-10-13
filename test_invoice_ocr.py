from datasets import load_dataset
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

print("Loading invoice dataset...")
ds = load_dataset("chainyo/rvl-cdip-invoice", split="train")

for i in range(5):
    image = ds[i]["image"].convert("RGB")
    text = pytesseract.image_to_string(image)

    print(f"\n--- Invoice {i + 1} ---")
    print(text[:500] if text.strip() else "No text detected")

print("\nOCR test completed.")