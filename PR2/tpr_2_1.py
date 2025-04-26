import matplotlib.pyplot as plt
import networkx as nx

# Представленная таблица
table = [
    [None, "1,8", None, None, None, None, None, None, None, "1,13"],
    [None, None, None, None, None, None, None, None, None, "1,67"],
    ["1,6", float('inf'), None, "2", None, None, None, None, None, "1,33"],
    [float('inf'), "2,8", "2,2", None, "2", None, "1,2", "1,8", "2,2", float('inf')],
    ["1,8", None, None, None, None, "3", None, "2,5", None, None],
    ["2,8", "2,8", "1,2", None, "2", None, "2,2", "1,8", float('inf'), "1,6"],
    [float('inf'), float('inf'), None, "2", None, None, None, float('inf'), "2,17", None],
    [float('inf'), float('inf'), "1,67", None, "2,5", "1,67", None, None, "4,67", "1,67"],
    [None, None, None, None, None, None, None, None, None, None],
    ["1,2", "1,2", None, None, None, None, None, None, None, None]
]

# Создание графа
G = nx.DiGraph()

# Добавление вершин
for i in range(len(table)):
    G.add_node(i + 1)

# Добавление рёбер между вершинами с числами или бесконечностью
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] is not None and table[i][j] != "∞":
            G.add_edge(i + 1, j + 1)

# Рисование графа
pos = nx.spring_layout(G)  # Определение позиций вершин
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray", width=2, connectionstyle="arc3,rad=0.1")

# Отображение графа
plt.title("Граф по таблице")
plt.show()
