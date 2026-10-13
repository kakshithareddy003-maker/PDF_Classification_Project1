from datasets import load_dataset
import pandas as pd

print("Loading receipt dataset...")
dataset = load_dataset("jsdnrs/ICDAR2019-SROIE")

records = []

for split_name in ["train", "test"]:
    for item in dataset[split_name]:
        text = " ".join(item["words"]).strip()

        if text:
            records.append({
                "text": text,
                "label": "Receipt",
                "split": split_name
            })

df = pd.DataFrame(records)
df.to_csv("receipt_data.csv", index=False, encoding="utf-8")

print("\nReceipt data saved successfully!")
print("Total records:", len(df))
print(df["split"].value_counts())
print("\nSample receipt text:")
print(df.iloc[0]["text"][:500])