import random
from itertools import combinations
import numpy as np

def euclidean_distance(a, b):
    distance = 0.0
    for i in range(len(a)): # if the space is multidimensional
        distance += (a[i] - b[i])**2
    return distance**(1/2)


def initialize_medoids(data, k):
    medoids = random.sample(data, k) # creates a sublist from the main list 'data'
    return medoids


def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        distances = [euclidean_distance(point, medoid) for medoid in centroids] # distance from the point to all centroids
        nearest_medoid_index = distances.index(min(distances)) # the point is nearest to some cluster
        clusters.append(nearest_medoid_index) # index of the nearest cluster
    return clusters


def calculate_new_medoids(data, clusters, k):
    new_medoids = []
    for i in range(k):
        cluster_points = [data[j] for j in range(len(data)) if clusters[j] == i]
        if cluster_points: # if the cluster has points assigned
            new_medoid = min(cluster_points, key=lambda medoid_candidate: sum(euclidean_distance(medoid_candidate, point) for point in cluster_points))
            # tries all points as possible candidates and calculates the distance from this point to all points
            # the point that has the minimum distance from all other points is selected as the new medoid
        else:
            new_medoid = random.choice(data)
        new_medoids.append(new_medoid)
    return new_medoids


def kmedoids(data, k, max_iterations=100):
    medoids = initialize_medoids(data, k)
    for _ in range(max_iterations): # first stop criterion
        clusters = assign_clusters(data, medoids)
        new_medoids = calculate_new_medoids(data, clusters, k)
        if new_medoids == medoids: # second stop criterion
            break
        medoids = new_medoids
    return medoids, clusters


def rand_index(true_labels, predicted_labels):
    pairs = list(combinations(range(len(true_labels)), 2)) # generating all possible pairs
    
    agree_same_cluster = 0
    agree_different_cluster = 0
    for i, j in pairs:
        same_cluster_true = true_labels[i] == true_labels[j]
        same_cluster_pred = predicted_labels[i] == predicted_labels[j]
        if same_cluster_true == same_cluster_pred:
            if same_cluster_true:
                agree_same_cluster += 1
            else:
                agree_different_cluster += 1
    
    rand_idx = (agree_same_cluster + agree_different_cluster) / len(pairs)
    return rand_idx


def monte_carlo_experiment(data, true_labels, k, num_trials):
    rand_indices = []

    for trial in range(num_trials):
        medoids, predicted_labels = kmedoids(data, k)
        rand_idx = rand_index(true_labels, predicted_labels)
        rand_indices.append(rand_idx)
    
    mean_rand_index = np.mean(rand_indices)
    std_rand_index = np.std(rand_indices)
    return mean_rand_index, std_rand_index


data = [
    [1.0, 2.0], [2.0, 2.5], [1.5, 3.0], # cluster 0
    [8.0, 8.0], [9.0, 9.0], [8.5, 8.5], # cluster 1
    [5.0, 1.0], [6.0, 1.5], [5.5, 2.0]  # cluster 2
]

true_labels = [0, 0, 0, 1, 1, 1, 2, 2, 2]

num_trials = 100
k = 3
mean_rand_idx, std_rand_idx = monte_carlo_experiment(data, true_labels, k, num_trials)

print(f"Monte Carlo K-Medoids Clustering Results ({num_trials} trials)")
print(f"Mean Rand Index: {mean_rand_idx:.4f}")
print(f"Standard Deviation of Rand Index: {std_rand_idx:.4f}")
