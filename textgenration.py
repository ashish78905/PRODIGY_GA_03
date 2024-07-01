import random
import re
from collections import defaultdict

# Step 1: Prepare the dataset
def preprocess_text(text):
    # Remove punctuation and convert to lower case
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    return words

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return preprocess_text(text)

# Step 2: Build the Markov Chain
def build_markov_chain(words):
    markov_chain = defaultdict(list)
    for i in range(len(words) - 1):
        markov_chain[words[i]].append(words[i + 1])
    return markov_chain

# Step 3: Generate Text
def generate_text(markov_chain, start_word, length=50):
    current_word = start_word
    generated_text = [current_word]
    
    for _ in range(length - 1):
        next_words = markov_chain.get(current_word, [])
        if not next_words:
            break
        current_word = random.choice(next_words)
        generated_text.append(current_word)
    
    return ' '.join(generated_text)

# Example usage
# Load and preprocess the dataset
dataset = load_dataset('dataset.txt')

# Build the Markov Chain
markov_chain = build_markov_chain(dataset)

# Generate text
start_word = random.choice(dataset)
generated_text = generate_text(markov_chain, start_word)
print(generated_text)
