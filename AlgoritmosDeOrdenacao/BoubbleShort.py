import random


def bouble(lista):
    for j in range(len(lista)):
        for i in range(len(lista) - j -1):
            if(lista[i] > lista[i+1]):
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux

lista =[]
for i in range(10):
    lista.append(random.randint(0,100))

bouble(lista)

print(lista)