# Day 5 Project — ML Systems

Three small machine learning systems built from scratch and with scikit-learn: a spam classifier, a Q-learning maze agent, and k-Means clustering.

```
day5_project/
├── spam_classifier.py   # Naive Bayes / Logistic Regression / SVM spam filter
├── qlearner.py           # Q-learning agent in a grid maze
└── clustering.py         # k-Means on the Iris dataset
```

## Requirements

```
pip install scikit-learn matplotlib
```

## Part A — spam_classifier.py

Trains a spam/ham text classifier.

- Downloads the SMS Spam Collection dataset
- Converts text to TF-IDF features
- Trains three models: Naive Bayes, Logistic Regression, SVM
- Prints precision, recall, and F1-score for each

Run:
```
python spam_classifier.py
```

SVM performs best, reaching ~99% accuracy.

## Part B — qlearner.py

Trains an agent to navigate a 5x5 grid maze using Q-learning.

- Grid has walls, a start (top-left), and a goal (bottom-right)
- Rewards: +100 for reaching the goal, -1 per step, -10 for hitting a wall
- Trains for 10,000 episodes using the Bellman update
- Prints the optimal path found after training

Run:
```
python qlearner.py
```

## Part C — clustering.py

Runs k-Means clustering on the Iris dataset, ignoring the true labels during clustering.

- Loads Iris features only
- Runs k-Means with k=3, using 10 random restarts to avoid bad initializations
- Maps each cluster to its majority true label
- Prints clustering accuracy (~89%)
- Saves a scatter plot to `clusters.png` if matplotlib is available

Run:
```
python clustering.py
```

## Notes

- All three scripts are self-contained — no config files needed.
- `spam_classifier.py` requires an internet connection to download the dataset.
- Results vary slightly between runs due to randomness in train/test splits and centroid initialization.