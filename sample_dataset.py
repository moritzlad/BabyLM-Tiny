import random
import os

TARGET_WORDS = 500_000
SNIPPET_SIZE = 10_000
NUM_SNIPPETS = TARGET_WORDS // SNIPPET_SIZE

files = os.listdir("./train_10M")
for file in files:
    with open(f"./train_10M/{file}", "r", encoding="utf-8") as f:
        words = f.read().split()

    total_words = len(words)

    if (total_words > TARGET_WORDS):
        max_start = total_words - SNIPPET_SIZE
        starts = random.sample(range(max_start), NUM_SNIPPETS)

        snippets = [words[start:start + SNIPPET_SIZE] for start in starts]

        sampled_words = [word for snippet in snippets for word in snippet]

        with open(f"./train_500k/{file}", "w+", encoding="utf-8") as f:
            f.write(" ".join(sampled_words))
    else: 
        print(f"File {file} has only {total_words} words, not enough to sample {TARGET_WORDS} words.")

    
