from transformers import AutoTokenizer
from rich import print
from collections import Counter

# Load the Qwen3 0.6B tokenizer
model_name = "Qwen/Qwen3-0.6B"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

with open("count_text.txt", "r") as f:
    text = f.read()

    # Method A: Get the token IDs directly
    tokens = tokenizer.encode(text)
    print(f"Token count: {len(tokens)}")

    # Method B: See the actual fragments (useful for debugging)
    fragments = tokenizer.tokenize(text)
    counts = Counter(fragments)
    print(f"Most common: {counts.most_common(10)}")
