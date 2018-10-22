import graf_1 as graf
import random
import numpy as np


count=int(input())

a=0
mass=[]
for i in range(count):
  mass.append(graf.i(random.randint(1,50)))
  a+=mass[i]


print("це резулт")
print(a/count)

print("dispers")
print(np.var(mass))