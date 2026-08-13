# Day 7 Project — NLP Systems

Three small standalone NLP scripts built for CS50 AI Day 7 (Natural Language Processing).

## Structure

```
day7_project/
├── parser.py       CFG sentence parser
├── generator.py    bigram/trigram text generator with perplexity
├── sentiment.py     TF-IDF + Logistic Regression sentiment classifier
└── requirements.txt
```

## Setup

```
pip install -r requirements.txt
```

`sentiment.py` also needs two NLTK datasets. The script downloads them automatically the first time you run it:

```
nltk.download("movie_reviews")
nltk.download("stopwords")
```

If automatic download fails, run this once in a Python shell:

```python
import nltk
nltk.download("movie_reviews")
nltk.download("stopwords")
```

## Part A — parser.py

Defines a small context-free grammar (S, NP, VP, PP, Det, N, V, P, Adj, Adv) and parses two example sentences with NLTK's `ChartParser`.

Run it:

```
python parser.py
```

Each sentence prints every valid parse tree it finds, plus a count of how many parses exist. More than one parse means the sentence is structurally ambiguous.

## Part B — generator.py

Builds bigram and trigram language models from a small built-in text corpus (no download needed). It:

- splits the corpus into train/test sentences
- builds `bigram_model` and `trigram_model` with Laplace (add-one) smoothing
- generates 5 sample sentences from each model
- prints perplexity for each model on the held-out test sentences

Run it:

```
python generator.py
```

Lower perplexity means the model predicts the test text better. Trigram usually produces more locally coherent phrases than bigram because it looks at two previous words instead of one, but with a small corpus it can also have higher perplexity since there is less data per context.

Swap in a bigger corpus (e.g. a Project Gutenberg book) by replacing the `text` variable with your own text.

## Part C — sentiment.py

Trains a sentiment classifier on NLTK's `movie_reviews` corpus (2000 labeled positive/negative reviews, same idea as the IMDB dataset).

Steps performed:

- lowercases text, strips punctuation, removes stopwords
- vectorizes with TF-IDF (`max_features=10000`)
- trains `LogisticRegression`
- prints precision/recall/F1 on a held-out test split
- prints the top 20 most positive and top 20 most negative words by model coefficient

Run it:

```
python sentiment.py
```

Typical accuracy on this dataset is around 82–86%. To push past 88%, try increasing `max_features`, adding bigrams (`ngram_range=(1,2)`), or tuning `C` in `LogisticRegression`.

## Notes for beginners

- All three scripts are self-contained — run each one independently.
- `parser.py` and `generator.py` need no internet access after installing packages.
- `sentiment.py` needs internet access once, to download the NLTK corpora.
- Feel free to swap the toy corpora in `parser.py` and `generator.py` for real text once you're comfortable with how each script works.