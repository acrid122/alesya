from math import dist #функция для декартого расстояния

def clusterize(file): #функция кластеризации, которая будет принимать название файла
    data = {tuple(map(float, line.split())) for line in open(file)} #6.412136 10.106562
    #print(data[:2]) #[(6.412136, 10.106562), (5.466008, 8.589759)]

    clusters = [] #список кластеров. [(список_точек_кластера, центр), () ...]
    while data: #пока множество точек непустое -> можно формировать кластеры
        cluster = [data.pop()] #беру одну точку из множества data, относительно которой буду строить кластер
        for points in cluster: #буду проходиться по точка в множестве кластер, чтобы для каждой точки находить соседей
            print(points)
            neighbours = {p for p in data if dist(p, points) <= 2} #перебираю все точки из множества data и беру только те, для которых расстояние от исходной точки меньше эпсилон
            cluster.extend(neighbours) #расширения списками текущими соседями
            data -= neighbours #убираю вычисленные точки соседей, чтобы не использовать их для других кластеров
        center = min(cluster, key = lambda point: sum(dist(point, p) for p in cluster)) #центроид
        clusters.append((cluster, center)) #добавляю в список кластер сформированный кластер
    return clusters

clustersA = clusterize('27A_27780.txt')
print(int(sum(dist((1.0, 1.5), center) for points, center in clustersA) * 10000))