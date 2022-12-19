opcio = 0
print ("""
Menú:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
0. Sortir
""")
opcio=input("Seleccionani l'opció que vulgui: ")
a = input("Indiqui el primer operand: ")
b = input("Indiqui el segon opernad: ")
match opcio: 
    case "1":
        c=int(a)+int(b)
        print("La suma de ",a," més ",b," és ",c)
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menys ",b," és ",c)
    case "3":
        c=int(a)*int(b)
        print("La multiplicació de ",a," por ",b," és ",c)
    case "4":
        c=int(a)/int(b)
        print("La divisió de ",a," menys ",b," és ",c)
    case "0":
        print("Adéu")
    case other: 
        print("Opció no vàlida")