cad = input("Introduce una cadena: ")
subcad = input("Introduce un carácter: ")
while subcad.isalnum() == False:
    print("Escriba un carácter alfanumérico por favor.")
    subcad = input("Introduce un carácter: ")
while len(subcad) != 1:
    print("Introduca 1 carácter por favor.")
    subcad = input("Introduce un carácter: ")
palabras = len(cad.split())
repetición = cad.count(subcad)
pos = []
for i,t in enumerate(cad):
    if t == subcad:
        pos.append(i)
print("La cadena consta de ",palabras," palabras.")
print("El carácter aparece ",repetición," veces.")
print("El carácter aparece en la posición: ",pos)