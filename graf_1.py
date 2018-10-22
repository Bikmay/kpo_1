import networkx as nx
import matplotlib.pyplot as plt
import random
import gist as g

def i(count_new):


    count=0

    count=count_new
   # n=int(input())

   # if(n==1):
    if(True):
        count = random.randint(1, 48)
    elif(n==2):
        count=int(input())

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
    count_handing_nodes=0
    #varitant 14
    mass_count_nodes=[]
    while(a<count):
        z=random.randint(0,4)
        a+=z
        mass_count_nodes.append(z)
        if(a>count):
            a-=z
            continue
        if(z==0):
            #считаем висячие
            count_handing_nodes+=1
            continue
        for j in range(z):
            r+=1
            mass_nodes.append(r)
            G.add_node(r)
            G.add_edge(mass_nodes[i],r)
        i+=1

    #Вывод массива верши
    print(mass_nodes)


    count_handing_nodes+=a-i+1

    #Та самая ебучая альфа из второго задания
    alpha=count/count_handing_nodes
    print("|")
    return alpha

    nx.draw(G, with_labels=True, node_color="blue", alpha=0.6, node_size=50)

    plt.savefig("edge_colormap.png")
    plt.show()


    g.create_gist(mass_count_nodes)





