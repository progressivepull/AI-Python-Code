import random
from collections import defaultdict

# 1. Sample Data (The "Corpus")
data = """
it was the best of times it was the worst of times
it was the age of wisdom it was the age of foolishness
"""

def build_model(text):
    words = text.lower().split()
    model = defaultdict(list)
    
    # Create pairs of (current_word, next_word)
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        model[current_word].append(next_word)
    return model

def predict_next(model, current_word):
    current_word = current_word.lower()
    if current_word in model:
        # Randomly pick from the list of observed next words
        return random.choice(model[current_word])
    else:
        return "Word not found in data."

# 2. Initialize and Run
word_model = build_model(data)
input_word = "the"
prediction = predict_next(word_model, input_word)

print(f"Input: '{input_word}'")
print(f"Predicted next word: '{prediction}'")
