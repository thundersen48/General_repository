import networkx as nx



edges = [(1, 2, {'weight': 4}),
         (1, 3, {'weight': 2}),
         (2, 3, {'weight': 1}),
         (2, 4, {'weight': 5}),
         (3, 4, {'weight': 8}),
         (3, 5, {'weight': 10}),
         (4, 5, {'weight': 2}),
         (4, 6, {'weight': 8}),
         (5, 6, {'weight': 5})]

edge_labels = {(1, 2): 4, (1, 3): 2, (2, 3): 1, (2, 4): 5, (3, 4): 8, (3, 5): 10, (4, 5): 2, (4, 6): 8, (5, 6): 5}
N = len(edges)

G = nx.Graph()
for i in range(1, 7):
    G.add_node(i)
G.add_edges_from(edges)

pos = nx.planar_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

fw = nx.floyd_warshall(G, weight='weight')

results = {a: dict(b) for a, b in fw.items()}
print(results)