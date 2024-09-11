import random

def euclidian_distance(a, b):
    distance = 0.0
    for i in range(len(a)): # if the space is multidimensional
        distance += (a[i] - b[i])**2
    return distance**(1/2)


def initialize_centroids(data, k):
    centroids = random.sample(data, k) # creates a sublist from the main list 'data'
    return centroids


def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        distances = [euclidian_distance(point, centroid) for centroid in centroids] # distance from the point to all centroids
        nearest_centroid_index = distances.index(min(distances)) # the point is nearest to some cluster
        clusters.append(nearest_centroid_index) # index of the nearest cluster
    return clusters


def calculate_new_centroids(data, clusters, k):
    new_centroids = []
    for i in range(k):
        cluster_points = [data[j] for j in range(len(data)) if clusters[j] == i]
        if cluster_points: # if the cluster has points assigned
            new_centroid = [sum(dimension) / len(cluster_points) for dimension in zip(*cluster_points)]
            # zip(*cluster_points) creates a list like this: [(x1, x2, x3), (y1, y2, y3)]
            # for each tuple the value is summed and divided by its lenght (mean)
        else:
            new_centroid = random.choice(data)
        new_centroids.append(new_centroid)
    return new_centroids


def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations): # first stop criterion
        clusters = assign_clusters(data, centroids)
        new_centroids = calculate_new_centroids(data, clusters, k)
        if new_centroids == centroids: # second stop criterion
            break
        centroids = new_centroids
    return centroids, clusters


data = [
    [1.0, 2.0], [2.0, 3.0], [3.0, 4.0],
    [2.5, 3.5], [0.0, 2.5], [4.0, 5.0]
]

k = 2 # number of clusters
centroids, clusters = kmeans(data, k)

print(f"Final centroids: {centroids}")
print(f"Data points assignment: {clusters}")
