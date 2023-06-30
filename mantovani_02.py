'''
17. En una carrera que tiene varios tramos, el ganador es aquel competidor que tarda menos en
llegar a la meta. Se mide el tiempo que tarda cada corredor en realizar cada tramo, esta medición se
toma en minutos. La cantidad de tramos no es fija.
Desarrolle un programa que permita ingresar los tiempos de un corredor de cada tramo y entregue
como resultado el tiempo total de carrera en formato horas:minutos.
El programa deja de pedir tiempos de tramos cuando se ingresa un 0.
Duracion tramo: 15
Duracion tramo: 30
Duracion tramo: 87
Duracion tramo: 0
Tiempo total de viaje: 2:12 horas
Duracion tramo: 51
Duracion tramo: 17
Duracion tramo: 0
Tiempo total de viaje: 1:08 horas

tiempo = 1
tiempo_total= 0

while tiempo != 0:
    tiempo=int(input("ingrese la duracion de un tramo: "))
    tiempo_total += tiempo



horas= tiempo_total // 60
minutos= tiempo_total % 60
print(f"Tiempo total de viaje: {horas}:{minutos}")


. Escriba un programa que entregue la suma de los primeros n números naturales, siendo n
ingresado por el usuario.
Matemáticamente lo que se pide que haga el programa es realizar la siguiente sumatoria.
S1=1+2+3+4+5+6+⋯+n
Además, obtenga el resultado de la siguiente fórmula.
S2=n×(n+1)/2
El programa debe entregar el resultado diciendo si S1 y S2 son iguales o no.
Ingrese n: 3
S1: 6
S2: 6
Son iguales

n = int(input("ingrese un numero: "))
s2= int(n*(n+1)/2)
s1= 0

for sumador in range (1, n+1):
    s1+=sumador


print(s1)
print(s2)
if s1== s2:
    print("son iguales")
else:
    print("no son iguales")

Escriba un programa que entregue todos los divisores del número entero ingresado:
Ingrese numero: 200
1 2 4 5 8 10 20 25 40 50 100 200

numerox= int(input("ingrese un numero: "))

for divisores in range(1, numerox+1):
    if numerox % divisores == 0:
        print(f" {divisores}")   
    
34. Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de
todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como
resultado 2 + 3 + 4 + 5 + 6 = 20.
Ingrese num: 1
Ingrese num: 7
La suma es 20
''' 

numero1= int(input("ingrese un numero: "))
numero2= int(input("ingrese ptro numero:"))
resultado=0

for sumatoria in range(numero1+1,numero2):
    resultado+= sumatoria
print(resultado)
