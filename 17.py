print("\n               Detector de Palindroms")
print("\nPalindrom = Paraula escrita igual d'esquerra a dreta")

a = input("\nInsereix el text: ")
text = a 

def palindrom(text):
    text = text[::-1]
    return text

print()
