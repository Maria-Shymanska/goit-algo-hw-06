import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (перехрестя)
G.add_nodes_from([1, 2, 3, 4, 5])

# Додавання ребер (дорог) з вагами
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=2)
G.add_edge(2, 3, weight=3)
G.add_edge(2, 4, weight=4)
G.add_edge(3, 4, weight=5)
G.add_edge(3, 5, weight=6)
G.add_edge(4, 5, weight=7)

# Візуалізація графа
nx.draw(G, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=labels)
plt.title("Транспортна мережа міста з вагами")
plt.show()

# Знаходження найкоротших шляхів між всіма парами вершин за допомогою алгоритму Дейкстри
shortest_paths = dict(nx.all_pairs_dijkstra(G))

# Вивід найкоротших шляхів між всіма парами вершин
print("Найкоротші шляхи між всіма парами вершин:")
for source in shortest_paths:
    for target, path_length in shortest_paths[source][0].items():
        print(f"Шлях від вершини {source} до вершини {target}: {path_length}")
