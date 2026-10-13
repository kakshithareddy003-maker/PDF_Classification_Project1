import pymupdf
import pandas as pd
from pathlib import Path

pdf_path = Path("electricity_bill_sample2.pdf")
output_path = Path("bill_data.csv")

if not pdf_path.exists():
    print("ERROR: electricity_bill_sample2.pdf was not found.")
    print("Make sure it is in your project folder.")
    raise SystemExit(1)

print("Reading electricity bill PDF...")

records = []

try:
    with pymupdf.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()

            if len(text) >= 50:
                records.append({
                    "text": text,
                    "label": "Bill"
                })

    if not records:
        print("No usable text found.")
        print("The PDF may be scanned and require OCR.")

    else:
        df = pd.DataFrame(records)
        df.to_csv(
            output_path,
            index=False,
            encoding="utf-8"
        )

        print("\nExtraction completed!")
        print("Pages extracted:", len(df))
        print("Saved to:", output_path.resolve())
        print("\nText preview:")
        print(df.iloc[0]["text"][:1500])

except Exception as error:
    print("Could not read the PDF:", error)