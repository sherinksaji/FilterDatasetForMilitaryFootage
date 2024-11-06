from datasets import load_from_disk

# Load the dataset from local disk
dataset = load_from_disk("panda-70m-train")

# Filter rows based on a query
# For example, let's filter for reviews that contain the word "excellent"
filtered_dataset = dataset.filter(lambda example: "soldier" in example["caption"])

# Display the filtered dataset
print(filtered_dataset)

print(filtered_dataset[:5])