def gran(x,y):
    a=x 
    if(x>y):
        print(x, "es mayor..." ,y)
    elif(y>x):
        print(y,"es mayor" ,x)
    else: 
        print(x,"y",y,"son lo mismo")
    return a


a=int(input("Escriure el primer valor: "))
b=int(input("Escriure el segon valor: "))
c=gran (a,b)
print("El más gran val: ",c)