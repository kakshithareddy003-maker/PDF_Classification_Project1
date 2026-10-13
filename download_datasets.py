from datasets import load_dataset

print("Loading receipt dataset...")
receipt_ds = load_dataset("jsdnrs/ICDAR2019-SROIE")

print("\nDataset splits:")
print(receipt_ds)

for split_name, split_data in receipt_ds.items():
    print(f"\nSplit: {split_name}")
    print("Rows:", len(split_data))
    print("Columns:", split_data.column_names)
    print("First example:")
    print(split_data[0])
    break