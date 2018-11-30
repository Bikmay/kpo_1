import graf_1 as graf
import random
import numpy as np

#count grafs
count=int(input())

a=0
mass=[]

count_nodes=0
n=int(input())
if(n==1):
   #  if(True):
    count_nodes = random.randint(1, 200)
elif(n==2):
     count_nodes=int(input())
handing_nodes = []
for i in range(count):
  mass.append(graf.i(count_nodes, handing_nodes=handing_nodes))
  a+=mass[i]


print("це резулт")
print(a/count)

print("dispers")
print(np.var(mass))

print("avr count handing nodes")
print(str(np.average(handing_nodes)))