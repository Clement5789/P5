from random import *
nombre = [0]*10
for i in range(1000):
    a=randint(1,10)
    nombre[a-1]+=1
print(nombre)