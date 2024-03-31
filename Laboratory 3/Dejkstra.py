import networkx as nx
import matplotlib.pyplot as plt
INF = 999999999
N = 5
def solve(start, graph):
    dlina = len(graph)
    path = [-1] * 5
    distance = [INF]*dlina
    distance[start] = 0

    visit = [False]*dlina
    for _ in range(dlina):
        min_dist = INF
        min_index = -1

        for i in range(dlina):
            if distance[i]<min_dist and not visit[i]:
                min_dist = distance[i]
                min_index = i

        visit[min_index] = True
        for j in range(dlina):
            if (not visit[j] and graph[min_index][j]!=INF and distance[min_index]+graph[min_index][j] < distance[j]):
                distance[j] = graph[min_index][j] + distance[min_index]
                path[j] = min_index

    return distance, path

G = nx.DiGraph()
G.add_nodes_from(range(N))

graph = [
    [0, 2, 5, INF, INF],
    [INF, 0, INF, INF, INF],
    [INF, INF, 0, 2, 7],
    [INF, INF, INF, 0, 3],
    [INF, INF, INF, INF, 0]
]

frs = []
scd = []
for i in range(N):
    for j in range(N):
        if graph[i][j]!=0 and graph[i][j]!=INF:
            G.add_edge(i, j)
            frs.append(i)
            scd.append(j)

start_vertex = 1
end_vertex = 5

distance, path = solve(start_vertex - 1, graph)
k = end_vertex - 1
npath = [k]

while npath[-1] != start_vertex-1:
    npath.append(path[npath[-1]])


npath.reverse()

path = npath
edge_colors = []
for i in range(N):
    for j in range(N - 1):
        if frs[j] > frs[j + 1] or frs[j] == frs[j+1] and scd[j] > scd[j+1]:
            k = frs[j+1]
            frs[j+1] = frs[j]
            frs[j] = k
            k = scd[j+1]
            scd[j + 1] = scd[j]
            scd[j] = k

path = npath
edge_colors = ["black"] * len(frs)

print("Путь: ", path)
print("Дистанция: ", distance)
for i in range(len(path) - 1):
    for j in range(len(frs)):
        if (path[i] == frs[j] and path[i + 1] == scd[j]):

            edge_colors[j] = "red"
            break


nx.draw(G, with_labels=True, edge_color=edge_colors)
plt.show()
