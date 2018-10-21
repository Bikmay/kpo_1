import matplotlib.pyplot as plt
import numpy as np



def create_gist(counts):

    #max_x= (count%10)+1
    x=[]

    #Самый бессмысленный цикл в мире
    for i in range(len(counts)):
        x.append(i)

   # i=1
   # for i in range(max_x):
   #    x.append(i*10)

    er=range(len(counts))
    ax=plt.gca()
    ax.bar(er,counts,align="edge")
    ax.set_xticks(er)


    print(len(counts))
    print(counts)
    #width=x
    #plt.bar(len(counts), counts, width,align="edge")
    #plt.xticks(x)
    plt.show()

 #  width = 1
  #  plt.bar(x,y, width)
   # plt.xticks(x)
    #plt.show()
