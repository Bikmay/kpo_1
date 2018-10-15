import networkx as nx
import matplotlib.pyplot as plt
import random

G=nx.Graph()

G.add_node(1)
count=random.randint(1,48)

r=int(count)

nx.draw(G,pos=nx.spectral_layout(G), nodecolor='r',edge_color='b')



def count_levels(num):
    count = 0
    level = 1
    i = 1
    if (num != 1):
        while (num > level):
            num -= level
            count += 1  
            level = level * 2

        if(num>1):
            count+=1
            return count
        else:
            print('else')
            return count_levels(random.randint(1, 48))



print(count_levels(r))

mass_nodes=[]

i=1
print(count)




print(mass_nodes)
G=nx.Graph()
G.add_node(1)
mass_nodes.append(1)
i=1
j=0
a=True
z=0
r=1
#varitant 14
while(i<=count):
    z=random.randint(1,5)
    for j in range(z):
        r+=1
        G.add_node(r)
        G.add_edge(i,r)
    i+=1


nx.draw(G, with_labels=True, node_color="blue", alpha=0.6, node_size=50)

plt.savefig("edge_colormap.png")
plt.show()






