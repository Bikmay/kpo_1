import matplotlib.pyplot as plt
import numpy as np



def create_gist(count):

    #max_x= (count%10)+1
    x=[1]
   # i=1
   # for i in range(max_x):
   #    x.append(i*10)
    ax=plt.gca()
    width=0.1
    plt.bar(1, count, width,align="edge")
    plt.xticks(x)
    plt.show()



create_gist(45)
#    x = [1,2,3,4]
 #  width = 1
  #  plt.bar(x,y, width)
   # plt.xticks(x)
    #plt.show()
