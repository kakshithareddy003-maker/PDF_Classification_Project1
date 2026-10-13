from datasets import load_dataset
import pytesseract
import pandas as pd

# Set the Tesseract OCR installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

print("Loading invoice dataset...")

# Load the invoice dataset
ds = load_dataset(
    "chainyo/rvl-cdip-invoice",
    split="train"
)

print("Total images available:", len(ds))

rows = []

# Process up to 1000 images
limit = min(1000, len(ds))

for i in range(limit):
    try:
        image = ds[i]["image"].convert("RGB")

        # Extract text using OCR
        text = pytesseract.image_to_string(image).strip()

        # Save readable text
        if len(text) >= 20:
            rows.append({
                "text": text,
                "label": "Invoice"
            })

        if (i + 1) % 50 == 0:
            print(
                f"Processed {i + 1}/{limit} images | "
                f"Readable invoices: {len(rows)}"
            )

    except Exception as e:
        print(f"Error processing image {i}: {e}")

# Convert results to a DataFrame
df = pd.DataFrame(rows)

# Save OCR data to CSV
df.to_csv(
    "invoice_ocr_data.csv",
    index=False,
    encoding="utf-8"
)

print("\nInvoice dataset preparation completed!")
print("Images processed:", limit)
print("Readable records saved:", len(df))
print("Output file: invoice_ocr_data.csv")