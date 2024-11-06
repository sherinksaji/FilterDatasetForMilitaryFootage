from datasets import load_dataset

# Load the dataset
dataset = load_dataset("SUSTech/panda-70m", split="train")

# Save it locally
dataset.save_to_disk("panda-70m-train")
