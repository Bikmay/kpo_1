import graf_1 as graf
import random
import numpy as np


count=int(input())

a=0
mass=[]
n=int(input())
if(n==1):
   #  if(True):
    count = random.randint(1, 200)
elif(n==2):
     count=int(input())
handing_nodes = []
for i in range(count):
  mass.append(graf.i(count, handing_nodes=handing_nodes))
  a+=mass[i]


print("це резулт")
print(a/count)

print("dispers")
print(np.var(mass))

print("avr count handing nodes")
print(str(np.average(handing_nodes)))