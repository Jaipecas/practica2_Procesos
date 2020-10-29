import multiprocessing
import math
import os


def calculo_raices(lista_numeros, lista_raices, suma_total):
    for i, numero in enumerate(lista_numeros):
        lista_raices[i] = math.sqrt(numero)

    suma_total.value = sum(lista_raices)
    print('ID del proceso en ejecución: {}'.format(os.getpid()))
    print("Las raices de las lista son: {}".format(lista_raices[:]))
    print("La suma de las raices de la lista es: {} ".format(suma_total.value))


if __name__ == "__main__":
    lista_numeros = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    lista_raices = multiprocessing.Array('d', 10)

    suma_total = multiprocessing.Value('d')

    p1 = multiprocessing.Process(target=calculo_raices, args=(lista_numeros, lista_raices, suma_total,))
    p2 = multiprocessing.Process(target=calculo_raices, args=(lista_numeros, lista_raices, suma_total,))

    p1.start()
    p2.start()

    print("ID del proceso p1: {}".format(p1.pid))
    print("ID del proceso p2: {}".format(p2.pid))

    p1.join()
    p2.join()

    print("Resultado en el main: ")
    print("Las raices de las lista son: {}".format(lista_raices[:]))
    print("La suma de las raices de la lista es: {}".format(suma_total.value))
