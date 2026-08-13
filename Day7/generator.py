import random
import math
from collections import defaultdict, Counter

text = """
the dog barked at the cat. the cat ran away. the dog chased the cat into the park.
a friend saw the dog in the park. the friend walked the dog. the dog was happy.
the cat climbed a tree. the dog barked at the tree. the friend laughed at the dog.
"""

sentences = [s.strip().split() for s in text.lower().replace(".", " .").split(".") if s.strip()]

def build_ngram_model(corpus, n):
    model = defaultdict(Counter)
    for sentence in corpus:
        tokens = ["<s>"] * (n - 1) + sentence + ["</s>"]
        for i in range(len(tokens) - n + 1):
            context = tuple(tokens[i:i + n - 1])
            next_word = tokens[i + n - 1]
            model[context][next_word] += 1
    return model

def probability(model, context, word, vocab_size, alpha=1):
    context = tuple(context)
    total = sum(model[context].values()) + alpha * vocab_size
    count = model[context].get(word, 0) + alpha
    return count / total

def perplexity(model, test_corpus, n, vocab_size):
    log_prob = 0
    total_words = 0
    for sentence in test_corpus:
        tokens = ["<s>"] * (n - 1) + sentence + ["</s>"]
        for i in range(n - 1, len(tokens)):
            context = tokens[i - (n - 1):i]
            word = tokens[i]
            log_prob += math.log(probability(model, context, word, vocab_size))
            total_words += 1
    return math.exp(-log_prob / total_words)

def generate_text(model, n, max_words=15):
    context = ["<s>"] * (n - 1)
    result = []
    for _ in range(max_words):
        ctx = tuple(context[-(n - 1):])
        if ctx not in model:
            break
        next_word = random.choices(list(model[ctx].keys()), weights=list(model[ctx].values()))[0]
        if next_word == "</s>":
            break
        result.append(next_word)
        context.append(next_word)
    return " ".join(result)

split = int(len(sentences) * 0.8)
train = sentences[:split]
test = sentences[split:]

vocab = set(word for sentence in sentences for word in sentence)
vocab_size = len(vocab)

bigram_model = build_ngram_model(train, 2)
trigram_model = build_ngram_model(train, 3)

print("Bigram generated sentences:")
for _ in range(5):
    print("-", generate_text(bigram_model, 2))

print()
print("Trigram generated sentences:")
for _ in range(5):
    print("-", generate_text(trigram_model, 3))

print()
print("Bigram perplexity:", perplexity(bigram_model, test, 2, vocab_size))
print("Trigram perplexity:", perplexity(trigram_model, test, 3, vocab_size))