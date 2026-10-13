import pandas as pd
from pathlib import Path

invoice_file = Path("invoice_ocr_data.csv")
receipt_file = Path("receipt_data.csv")

# Check that both files exist
if not invoice_file.exists() or not receipt_file.exists():
    print("Error: Could not find one or both CSV files.")
else:
    invoices = pd.read_csv(invoice_file)
    receipts = pd.read_csv(receipt_file)

    # Keep the required columns
    invoices = invoices[["text", "label"]]
    receipts = receipts[["text", "label"]]

    # Combine the datasets
    data = pd.concat(
        [invoices, receipts],
        ignore_index=True
    )

    # Clean empty records
    data = data.dropna(subset=["text"])
    data["text"] = data["text"].astype(str).str.strip()
    data = data[data["text"] != ""]

    # Remove exact duplicate text records
    data = data.drop_duplicates(subset=["text"])

    # Save the combined data
    data.to_csv(
        "combined_document_data.csv",
        index=False,
        encoding="utf-8"
    )

    print("Dataset prepared successfully!")
    print("Total unique records:", len(data))
    print("\nRecords per category:")
    print(data["label"].value_counts())
    print("\nSaved as combined_document_data.csv")