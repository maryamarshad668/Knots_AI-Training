import nltk
from nltk import CFG, ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det Adj N | NP PP | "she"
VP -> V | V NP | V PP | VP PP
PP -> P NP
Det -> "the" | "a"
N -> "dog" | "cat" | "park" | "friend" | "telescope"
V -> "barked" | "walked" | "saw"
P -> "in" | "with" | "at"
Adj -> "big" | "small"
Adv -> "quickly" | "quietly"
""")

parser = ChartParser(grammar)

sentences = [
    "the dog barked at the cat",
    "she walked in the park with a friend"
]

for sentence in sentences:
    words = sentence.split()
    print("Sentence:", sentence)
    count = 0
    for tree in parser.parse(words):
        tree.pretty_print()
        count += 1
    print("Number of parses:", count)
    print()