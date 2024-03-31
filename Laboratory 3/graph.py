import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite.gexf import GEXFReader

G = nx.DiGraph()
G.add_nodes_from(range(5))
G.add_edge(0,3)
G.add_edge(4,3)
G.add_edge(3,0)
G.add_edge(4,1)
G.add_edge(2,4)
G.add_edge(1,2)
path = [1, 2, 4, 3]

edge_colors = []
frs = [0, 4, 3, 4, 2, 1]
scd = [3, 3, 0, 1, 4, 2]
for i in range(6):
    for j in range(5):
        if frs[j] > frs[j + 1] or frs[j] == frs[j+1] and scd[j] < scd[j+1]:
            k = frs[j+1]
            frs[j+1] = frs[j]
            frs[j] = k
            k = scd[j+1]
            scd[j + 1] = scd[j]
            scd[j] = k

edge_colors = ["black"] * 6
print(frs)
print(scd)
for i in range(len(path) - 1):
    for j in range(6):
        if (path[i] == frs[j] and path[i + 1] == scd[j]):
            print(j, path[i], path[i+1])
            edge_colors[j] = "red"
            break



print(edge_colors)
nx.draw(G, with_labels=True, edge_color=edge_colors)
plt.show()

print(G)