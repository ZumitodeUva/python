def sumar_llista (a):
    sumatori=0 
    for i in a:
        sumatori+= i 
    return sumatori


def multiplicar_lista (lista):
    multiplicado=1
    for y in lista:
        multiplicado = multiplicado + (y*y)
    return multiplicado

x=[1, 3 , 4, 5, 7, 8, 15, 33]
print("La suma dels elements de la llista és: ", sumar_llista(x))
print("La multiplicació dels elements de la llista és: ", multiplicar_lista(x))