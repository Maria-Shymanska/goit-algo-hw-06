import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (перехрестя)
G.add_nodes_from([1, 2, 3, 4, 5])

# Додавання ребер (дорог)
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Візуалізація графа
nx.draw(G, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Список ребер:", list(G.edges()))
print("Ступінь вершин:", dict(G.degree()))
