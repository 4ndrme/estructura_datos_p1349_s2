import bisect
import time
matriz = [i for i in range(1, 1000001)]

numero =int(input("Ingrese el numero que desa buscar: "))

timpo_in = time.perf_counter()

busqueda=bisect.bisect_left(matriz, numero)

tiempo_fi=time.perf_counter()
tiempo_total= tiempo_fi - timpo_in

print("|||||||||||||||RESULTADOS-NUMERO Y TIEMPO|||||||||||||||")
if busqueda < len(matriz) and matriz[busqueda] == numero:
    print(f"El numero {numero}, encontrado en la posicion {busqueda}")
else:
    print(f"El numero {numero} no se encuentra en la matriz")
print(f"El timepo total de la busqueda fue de {tiempo_total:.8f}")



