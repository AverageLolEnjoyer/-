import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    heapq.heapify(queue)
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            path = path + [node]
            seen.add(node)
            if node == end:
                return (cost, path)
            for next_node, weight in enumerate(graph[node]):
                if weight and next_node not in seen:
                    total_cost = cost + weight
                    heapq.heappush(queue, (total_cost, next_node, path))
    return float("inf"), []


def yen(graph, start, end, K):
    A, _ = dijkstra(graph, start, end)  # Найдем первый наилучший путь
    result = [(A, dijkstra(graph, start, end)[1])]

    for k in range(1, K):
        for i in range(len(result[k-1][1]) - 1):
            spur_node = result[k-1][1][i]
            root_path = result[k-1][1][:i+1]
            edges_removed = []

            for path in result:
                if len(path[1]) > i and root_path == path[1][:i+1]:
                    graph[path[1][i]][path[1][i+1]] = float("inf")
                    edges_removed.append((path[1][i], path[1][i+1], graph[path[1][i]][path[1][i+1]]))

            spur_cost, spur_path = dijkstra(graph, spur_node, end)

            if spur_path:
                total_path = root_path[:-1] + spur_path
                total_cost = sum(graph[total_path[j]][total_path[j+1]] for j in range(len(total_path)-1))
                heapq.heappush(result, (total_cost, total_path))

            for edge in edges_removed:
                graph[edge[0]][edge[1]] = edge[2]

        if not result:
            break

    return result


# Пример матрицы весов
graph_matrix = [
    [0, 5, 4, 2, 7, 0, 0],
    [0, 0, 0, 5, 12, 3, 20],
    [0, 1, 0, 0, 3, 7, 0],
    [0, 1, 0, 0, 4, 6, 15],
    [0, 4, 5, 0, 0, 11, 0],
    [0, 6, 0, 0, 0, 0, 2],
    [0, 0, 3, 0, 8, 0, 0]
]

start_node = 0
end_node = 6
K = 3

result = yen(graph_matrix, start_node, end_node, K)
for i in range(K):
    print(result[i])