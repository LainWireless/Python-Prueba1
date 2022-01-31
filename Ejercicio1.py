from math import sqrt
print("Se va a resolver la siguiente ecuación: ax² + bx + c = 0")
a = int(input("Coeficiente de a: "))
b = int(input("Coeficiente de b: "))
c = int(input("Coeficiente de c: "))
if a == 0:
    x = -c/b
    print("Solución: ",x)
elif b*b - 4*a*c < 0:
    print("Raíces complejas.")
else:
    discriminante = b*b - 4*a*c
    raiz = sqrt(discriminante)
    x1 = (-b + raiz) / (2 * a)
    if discriminante != 0:
        x2 = (-b - raiz) / (2 * a)
        print("Solución 1: ",x1)
        print("Solución 2: ",x2)
    else:
        print("Solución: ",x1)