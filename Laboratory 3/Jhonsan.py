
INF = 9999999
def Jhonsan(graph):

    n = len(graph)
    dist = [INF]*n
    dist[n - 1] = 0
    for _ in range(n - 1):
        for i in range(n):
            for j in range(n):
                if (graph[i][j]!= INF):
                    if (dist[j] > dist[i] + graph[i][j]):
                        dist[j] = graph[i][j] + dist[i]
    n -= 1

    for i in range(n):
        for j in range(n):
            if(graph[i][j]!=INF):
                graph[i][j] = graph[i][j] + dist[i] - dist[j]
    for i in graph:
        print(i)
    for st in range(n):
        dlina = n
        start = st
        distance = [INF] * dlina
        distance[start] = 0

        visit = [False] * dlina
        for _ in range(dlina):
            min_dist = INF
            min_index = -1
            for i in range(dlina):
                if distance[i] < min_dist and not visit[i]:
                    min_dist = distance[i]

                    min_index = i
            if (min_index == -1):
                print(distance)
                break
            visit[min_index] = True
            for j in range(dlina):
                if ((not visit[j]) and graph[min_index][j] != INF and distance[min_index] + graph[min_index][j] <
                        distance[j]):

                    distance[j] = graph[min_index][j] + distance[min_index]
        else:
            print(distance)


graphb = [
    [0, -4, INF, 1, -2, INF],
    [INF, 0, 5, INF, INF, INF],
    [2, INF, 0, INF, INF, INF],
    [INF, INF, INF, 0, 3, INF],
    [INF, INF, INF, INF, 0, INF],
    [0, 0, 0, 0, 0, 0]
]

Jhonsan(graphb)