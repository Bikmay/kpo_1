import networkx as nx
import random

G=nx.Graph()

G.add_node(1)
#count=random.randint(1,48)
#count=input()
#r=int(count)

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



#print(count_levels(r))






