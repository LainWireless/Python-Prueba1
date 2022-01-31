valor = 0
mayor = 0
cont = 0
preguntas = int(input("¿Cuántas edades en años quiere introducir?: "))
total = preguntas
while preguntas <= 0:
    print("Debe introducir al menos 1.")
    preguntas = int(input("¿Cuántas edades en años quiere introducir?: "))
while preguntas > 0:
    edad = int(input("Introduzca una edad: "))
    while edad < 0:
        print("La edad no puede ser menor que 0.")
        edad = int(input("Introduzca una edad: "))
    while edad >= 100:
        print("La edad debe ser menor que 100.")
        edad = int(input("Introduzca una edad: "))
    valor = valor+int(edad)
    if edad > mayor:
        mayor = edad
    if edad >= 18:
        cont = cont +1
    preguntas = preguntas -1
    media = valor/total
print("La mayor edad introducida ha sido: ",mayor)
print("La media de todas las edades es: ",media)
print("Cantidad de edades mayores de 18: ",cont)