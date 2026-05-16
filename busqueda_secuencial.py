import time

matriz = [i for i in range(1, 1000001)]

numero = int(input("Ingrese el numero que desea buscar: "))
timpo_in = time.perf_counter()

busqueda = -1
for posicion, elemento in enumerate(matriz):
    if elemento == numero:
        busqueda = posicion
        break 

tiempo_fi = time.perf_counter()
tiempo_total = tiempo_fi - timpo_in

print("|||||||||||||||RESULTADOS-NUMERO Y TIEMPO|||||||||||||||")
if busqueda != -1:
    print(f"El numero {numero}, encontrado en la posicion {busqueda}.")
else:
    print(f"El numero {numero} no se encuentra en la matriz")

print(f"El tiempo total de la busqueda fue de {tiempo_total:.8f} segundos")
