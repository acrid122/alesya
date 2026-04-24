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
        center = min(cluster, key = lambda point: 
                     sum(dist(point, n_point) for n_point in cluster))
        clusters.append((cluster, center))
    return clusters

clustersA = clusterize('27A_27780.txt', 1)
A1 = len(max(clustersA, key = lambda cluster: len(cluster[0]))[0])
A2 = sum(dist((1.0, 1.5), center) for _, center in clustersA)
print(A1, int(A2 * 10000))


#clustersB = [(список_точек_в_кластере, центр), (), ()]

clustersB = clusterize('27B_27780 (1).txt', 1)
clustersB.sort(key = lambda cluster: len(cluster[0]))
B1 = sum(1 for point in clustersB[1][0] 
         if dist(clustersB[1][1], point) <= 1.2 and \
            point != clustersB[1][1])
B2 = float('inf')
for point in clustersB[2][0]:
    if point != clustersB[2][1]:
        B2 = min(B2, dist(point, clustersB[2][1]))
print(B1, int(B2 * 10000))


def clusterize_anomaly(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neighbours = {i for i in data if dist(i, point) <= eps}
            cluster.extend(neighbours)
            data -= neighbours
        if len(cluster) > 10: #обработка аномалий
            center = min(cluster, key = lambda point:
                         sum(dist(point, n_point) for n_point in cluster))
            clusters.append((cluster, center))
    return clusters

clustersA = clusterize_anomaly('27A_27593 (1).txt', 2)
Px = float('inf')
for _, center in clustersA:
    Px = min(dist(center, (5.5, 9.1)), Px)

centerA1 = clustersA[0][1]
centerA2 = clustersA[1][1]
Py = dist((5.5, 9.1), ((centerA1[0] + centerA2[0]) / 2, 
                       (centerA1[1] + centerA2[1]) / 2))

print(int(Px * 10000), int(Py * 10000))


clustersB = clusterize_anomaly('27B_27593 (1).txt', 2)
clustersB.sort(key = lambda cluster: len(cluster[0]))
center_maxB = clustersB[2][1]
center_minB = clustersB[0][1]
Q1, Q2 = 0, 0
for cluster, _ in clustersB:
    for point in cluster:
        if dist(point, center_maxB) <= 10:
            Q1 += 1
        if dist(point, center_minB) > 5:
            Q2 += 1

print(Q1, Q2)

