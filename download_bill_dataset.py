from datasets import load_dataset

dataset = load_dataset("prithivMLmods/Document-Type-Detection")
train_data = dataset["train"]

print("Total images:", len(train_data))
print("\nAvailable labels:")

label_feature = train_data.features["label"]

if hasattr(label_feature, "names") and label_feature.names:
    print(label_feature.names)
else:
    print(sorted(set(train_data["label"])))

print("\nFirst 5 label values:")
print(train_data["label"][:5])