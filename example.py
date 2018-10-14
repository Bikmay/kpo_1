import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()

G.add_node(1)


G.add_node(2)


G.add_node(3)
G.add_edge(1,3)

nx.draw(G, with_labels=True, node_color="blue", alpha=0.6, node_size=50)

plt.savefig("edge_colormap.png")
plt.show()