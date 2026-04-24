from math import *

def clusterize(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neighbours = {i for i in data if dist(i, point) <= eps}
            cluster.extend(neighbours)
            data -= neighbours
        maxd = float('-inf')
        for i in range(len(cluster)):
            for j in range(i + 1, len(cluster)):
                if maxd <= dist(cluster[i], cluster[j]):
                    diameter = (cluster[i], cluster[j])
                    maxd = dist(cluster[i], cluster[j])
        clusters.append((cluster, diameter))
    return clusters

clustersA = clusterize('27A_27591 (1).txt', 1)
Px = float('inf')
for _, diameter in clustersA:
    Px = min(Px, diameter[0][0] + diameter[1][0])
Py = float('-inf')
for _, diameter in clustersA:
    Py = max(Py, diameter[0][1] + diameter[1][1])
print(int(Px * 10000), int(Py * 10000))

def clusterize1B(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neighbours = {i for i in data if dist(i, point) <= eps}
            cluster.extend(neighbours)
            data -= neighbours
        if len(cluster) > 10: #обработка аномалий
            maxd = float('-inf')
            for i in range(len(cluster)):
                for j in range(i + 1, len(cluster)):
                    if maxd <= dist(cluster[i], cluster[j]):
                        diameter = (cluster[i], cluster[j])
                        maxd = dist(cluster[i], cluster[j])
            clusters.append((cluster, diameter))
    return clusters

clustersB = clusterize1B('27B_27591 (1).txt', 1)
print(len(clustersB))
s_clustersB = sorted(clustersB, key = lambda cluster: len(cluster[0]))
min_clusterB = s_clustersB[0]
Q1 = dist(*min_clusterB[1])
print(int(Q1 * 10000))

Q2 = float('-inf')
for _, diameter in clustersB:
    for _, diameter2 in clustersB:
        '''
        ((20.1299441, 25.8980112), (23.1257571, 23.3363392)) 
        ((20.1299441, 25.8980112), (23.1257571, 23.3363392))
        '''
        Q2 = max(
            Q2,
            dist(diameter[0], diameter2[0]),
            dist(diameter[0], diameter2[1]),
            dist(diameter[1], diameter2[0]),
            dist(diameter[1], diameter2[1]),
        )
print(int(Q2 * 10000))

from math import *
def clust(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neighbour = {i for i in data if dist(i, point) <= eps}
            cluster.extend(neighbour)
            data -= neighbour
        anti_center = max(cluster, key = lambda point: sum(dist(point, n_point) for n_point in cluster))
        clusters.append((cluster, anti_center))
    return clusters

clustersA = clusterize('27A_27590 (1).txt', 1)
#[( [(), (), ()], (anti_center_x, anti_center_y)), (), ..]
s_clustersA = sorted(clustersA, key = lambda cluster: len(cluster[0]))


