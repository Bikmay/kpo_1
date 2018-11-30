import networkx as nx
import matplotlib.pyplot as plt
import random
import gist as g
#from docx import *

#https://python-docx.readthedocs.io/en/latest/

def i(count_new, handing_nodes = []):




    count=count_new
   #  n=int(input())
   #  if(n==1):
   # #  if(True):
   #      count = random.randint(1, 200)
   #  elif(n==2):
   #      count=int(input())

    print(count)
    G=nx.Graph()

    G.add_node(1)


    r=count

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


    #Количество уровней в графе
    print(count_levels(r))

    #массив вершин
    mass_nodes=[]

    #вывод количества  вершин
    print(count)





    #Инициализация графа, создание первой ноды
    G=nx.Graph()
    G.add_node(1)
    mass_nodes.append(1)

    i=0
    j=0
    z=0
    r=1
    a=1
    mass2=[]
    count_handing_nodes=0
    #varitant 14
    mass_count_nodes=[]

    o9=0
    _2=[]


    while(a<count):
        z=random.randint(0,4)
        a+=z
        mass_count_nodes.append(z)
        if(a>count):
            a-=z
            continue
        else:
            _2.append(z)
        if(z==0):

            mass2.append(mass_nodes[i-1])
            i+=1
            continue

        o9=0
        for j in range(z):
            r+=1
            mass_nodes.append(r)
            G.add_node(r)
            G.add_edge(mass_nodes[i],r)

            print(str(mass_nodes[i])+'-'+str(r), end=", ")
        i+=1

    #Вывод массива верши
    print(mass_nodes)


    count_handing_nodes+=a-i+1
    ou=count_handing_nodes-count_handing_nodes*2

   # n_mass=mass_nodes[-1:ou]

   # print(n_mass)
    print('zz')
    for a in range(len(_2)):
        if(_2[a]==0):
            print(a)


   # for u in range(len(n_mass)):
     #   mass2.append(n_mass[u])

    alpha=count/count_handing_nodes
    print("alpha: " + str(alpha))


    nx.draw(G, with_labels=True, node_color="blue", alpha=0.6, node_size=50)

    plt.savefig("edge_colormap.png")
    plt.show()



    g.create_gist(_2)
    return alpha




