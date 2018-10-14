import matplotlib.pyplot as plt
import numpy as np



def create_gist(d):
    x = [1,2,3,4]
    y = d
    width = 1
    plt.bar(x,y, width)
    plt.xticks(x)
    plt.show()
