#Definició de funcions auxiliars
def menu_principal():
    print("""Calculadora
    Menú:
    1. Números enters
    2. Números reals
    3. Canvis de base
    0. Sortir
""")
opcio=input("Seleccioni l'opció que vulgui: ")


# Funció del menú de numeros enters

def menu_enters():
    print("""
        Menú calculadora de números enters:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Potència
        6. Mòdul
        0. Sortir
         """)
opcio=input("Seleccioni l'opció que vulqui: ")

# Funció del menú dels canvis de base 
def menu_canvis_base():
    print ("""
            Menú calculadora canvis de base:
            1. Donat un binari passar a octal, decimal i hexadecimanl.
            2. Donat un octal passar a binari, decimal i hexadecimal
            3. Donat un decimal passar a binari, octal i hexadecimal
            4. Donat un hexadecimal passar a binari, ocatl i decimal
            0. Sortir
            """)
opcio=input("Seleccioni l0opció que vulgui: ")

#Funció del menú dels números reals
def menu_reals():
    print("""`
            Menú calculadora de números reals:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potència
            0. Sortir
            """)
opcio2=input("Seleccioni l'opció que vulgui: ")

# Programa principal de la calculadora
opcio=1
while(opcio!=0):
    opcio=menu_principal()
    match opcio:
        case "1":
            opcio2=menu_enters()
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))
            match opcio2:
                case "1":
                    c=a+b
                    print("La suma de ",a," més ",b," és ",c)
                case "2": 
                    c=a-b
                    print("La resta de ",a," menys ",b," és ",c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ",c)
                case "4":
                    c=a/b
                    print("La divisió de ",a," per ",b," és ",c)
                case "5":
                    c=a ** b
                    print("La potència de ",a," elevat a ",b," és ",c)
                case "6":
                    c = a % b 
                    print("El mòdul de ",a," per ",b," és ",c)
                case "0":
                    print("Adéu")
                case other:
                    print("Opció no vàlida!")

        case "2": 
