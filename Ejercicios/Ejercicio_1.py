# # --------------------- EJERCICIO 1 ----------------------------------
# # Variables numéricas
# edad = int(input('Ingrese la edad: '))  # Entero
# altura = float(input('Ingrese la Altura: '))  # Flotante
# peso = float(input('Ingrese el Peso: ')) # Flotante

# # Operaciones matemáticas
# imc = peso / (altura ** 2)  # Cálculo del índice de masa corporal

# # Mostrar resultados
# print("Edad actual:", edad)
# print("IMC:", round(imc, 2))  # Redondear a 2 decimales

# print("Edad actual:" + str(edad))

# x = input('Ingrese un valor: ')

# # --------------------- EJERCICIO 2 ----------------------------------

# Solicitar los puntos al usuario
x1 = float(input("Ingresa la coordenada x1: "))
y1 = float(input("Ingresa la coordenada y1: "))
x2 = float(input("Ingresa la coordenada x2: "))
y2 = float(input("Ingresa la coordenada y2: "))

# Calcular la pendiente (m)
m = (y2 - y1) / (x2 - x1)
print("La pendiente de la recta es: {}, {}".format(round(m, 2), 5))




# --------------------- EJERCICIO 3 ----------------------------------
x = 0
x += 3
print(x)



for x in items:
    if condition:
    [do this ... ]
    break
    do this
do this when loop is finished


