
def floyd_warshall(graphb):
    graph = graphb
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(graph[i][j] > graph[i][k] + graph[k][j]):
                    graph[i][j] = graph[i][k]+ graph[k][j]
    return graph
INF = 999

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

res = floyd_warshall(graph)

start_vertex = 1
end_vertex = 8

print("Расстояние от вершины ", start_vertex, "до вершины ", end_vertex," равна ",res[start_vertex-1][end_vertex-1])