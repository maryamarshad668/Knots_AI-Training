import random
import math
from collections import Counter
from sklearn.datasets import load_iris

def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def kmeans(X, k, max_iter=100):
    centroids = random.sample(X, k)
    clusters = [[] for _ in range(k)]
    assignments = [0] * len(X)

    for _ in range(max_iter):
        clusters = [[] for _ in range(k)]
        assignments = []
        for point in X:
            nearest = min(range(k), key=lambda i: euclidean(point, centroids[i]))
            clusters[nearest].append(point)
            assignments.append(nearest)

        new_centroids = []
        for cluster in clusters:
            if cluster:
                mean = [sum(dim) / len(cluster) for dim in zip(*cluster)]
                new_centroids.append(mean)
            else:
                new_centroids.append(random.choice(X))

        if new_centroids == centroids:
            break
        centroids = new_centroids

    return centroids, clusters, assignments

def inertia(X, centroids, assignments):
    return sum(euclidean(X[i], centroids[assignments[i]]) ** 2 for i in range(len(X)))

X, y_true = load_iris(return_X_y=True)
X = X.tolist()
y_true = y_true.tolist()

best_result = None
best_inertia = None
for _ in range(10):
    centroids, clusters, assignments = kmeans(X, k=3)
    current_inertia = inertia(X, centroids, assignments)
    if best_inertia is None or current_inertia < best_inertia:
        best_inertia = current_inertia
        best_result = (centroids, clusters, assignments)

centroids, clusters, assignments = best_result

cluster_to_label = {}
for cluster_id in range(3):
    true_labels = [y_true[i] for i in range(len(X)) if assignments[i] == cluster_id]
    if true_labels:
        majority = Counter(true_labels).most_common(1)[0][0]
        cluster_to_label[cluster_id] = majority

correct = 0
for i in range(len(X)):
    predicted_label = cluster_to_label[assignments[i]]
    if predicted_label == y_true[i]:
        correct += 1

accuracy = correct / len(X)
print("cluster to majority label mapping:", cluster_to_label)
print("clustering accuracy:", accuracy)

try:
    import matplotlib.pyplot as plt
    colors = ["r", "g", "b"]
    for i in range(len(X)):
        plt.scatter(X[i][0], X[i][1], c=colors[assignments[i]])
    plt.xlabel("sepal length")
    plt.ylabel("sepal width")
    plt.title("k-Means clusters on Iris")
    plt.savefig("clusters.png")
    print("plot saved to clusters.png")
except ImportError:
    print("matplotlib not available, skipping plot")