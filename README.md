#Descripcion general
Este repositorio se creó con el propósito de realizar diferentes tipos de búsquedas en una lista que va desde `1` hasta `1.000.000`. Como entrada, el número será ingresado por el usuario en la terminal y la salida será desplegada en la misma; esto, junto al uso del módulo time, que sirve para medir el tiempo, permitirá una comparación entre los dos métodos de búsqueda Para esto se crearon dos programas que realizan dos búsquedas de diferente manera, para conocer la diferencia entre los dos tipos de búsqueda.

##busqueda_binaria:
Este programa busca el número ingresado de manera binaria, esto gracias a la integración del módulo `bisect` que viene en la librería de Python. Este módulo contiene las herramientas para usar algoritmos que permiten la búsqueda binaria de manera más eficiente, encontrando el número ingresado en un máximo de 20 pasos. Además, contiene el módulo time; este sirvió para medir el tiempo que el programa se tarda en encontrar el número ingresado.

##busqueda_secuencial:
A diferencia del anterior, aquí se hace la búsqueda de manera más tradicional, puesto que no se usa el módulo bisect; por lo mismo, este usa un método secuencial o lineal de búsqueda, en donde el número ingresado tendrá que ser buscado en un recorrido que será de toda la lista, es decir, que si se ingresa el número 999.999, el programa tendrá que recorrer casi 1M de pasos para mostrar el número De igual manera, este contiene el módulo time para medir el tiempo que este tipo de búsqueda tarda.

##Instrucciones de uso:
El uso de estos dos programas es igual; al ejecutar el programa, se pedirá el ingreso de un número en la terminal; posterior a esto, se desplegará el resultado, mostrando la posición en la que se encontró y el tiempo que se tardó el programa en encontrarlo.

## Pre requisitos:
- Python 3.14
- VS code    

##Resultados esperados:
Los resultados esperados mostraron que el programa que usa el módulo bisect para la búsqueda binaria tiene un más de rapidez que el programa que usa el método de búsqueda secuencial. Como un ejemplo, se ingresó el número `500.000`, en donde los resultados fueron:
** Busqueda binaria **
- Tiempo: `0.00001280`
** Busqueda binaria **
- Tiempo: `0.03211430`
** Resultados **
La diferencia entre estos resultados mostró una diferencia aproximada de 32 milisegundos entre el método de búsqueda binaria frente al método secuencial, lo cual podrá sonar mínimo para nosotros, pero que en realidad es una diferencia enorme en campos más avanzados de manejo de datos.
