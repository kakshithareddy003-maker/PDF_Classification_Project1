import pandas as pd
from pathlib import Path

# Read the OCR text extracted from bill3.png
text_path = Path("bill3_receipt_text.txt")
csv_path = Path("receipt_data.csv")

if not text_path.exists():
    print("Error: bill3_receipt_text.txt was not found.")
elif not csv_path.exists():
    print("Error: receipt_data.csv was not found.")
else:
    text = text_path.read_text(encoding="utf-8").strip()

    if not text:
        print("Error: No text was extracted.")
    else:
        df = pd.read_csv(csv_path)

        new_record = pd.DataFrame([{
            "text": text,
            "label": "Receipt",
            "split": "extra"
        }])

        # Keep only columns that exist in the original CSV
        new_record = new_record.reindex(columns=df.columns)
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_csv(csv_path, index=False, encoding="utf-8")

        print("Receipt added successfully!")
        print("Total records:", len(df))
        print("Saved to:", csv_path.resolve())