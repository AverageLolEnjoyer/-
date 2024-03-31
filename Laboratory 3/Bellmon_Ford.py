INF = 9999999
def bellman_ford(start, graph):
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0

    for _ in range(n - 1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] != INF:
                    if dist[i] + graph[i][j] < dist[j]:
                        dist[j] = dist[i] + graph[i][j]
        print(dist)
    return dist

graph = [
    [0, 6, 1, INF, INF, INF, INF, INF],
    [INF, 0, INF, INF, INF, INF, 4, INF],
    [INF, INF, 0, 4,INF, 2, INF, INF],
    [INF, INF, INF, 0, 6 , INF, INF, INF],
    [INF, INF, INF, INF, 0 , INF, INF,  INF],
    [INF, 2, INF, INF, INF, 0, INF , 18],
    [INF, INF, INF, INF, INF, 1, 0, 5],
    [INF, INF,  INF, INF, INF, INF, INF, 0]
]

start_vertex = 1

res = bellman_ford(start_vertex - 1, graph)
print(res)