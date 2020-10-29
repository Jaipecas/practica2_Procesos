import math
import multiprocessing

lista_raices = []
suma_total = 0


def calculo_raices(lista_numeros):
    global lista_raices
    global suma_total

    for numero in lista_numeros:
        lista_raices.append(math.sqrt(numero))

    suma_total = sum(lista_raices)

    print("Las raices de las lista son: {}".format(lista_raices))
    print("La suma de las raices de la lista es: {} ".format(suma_total))


if __name__ == "__main__":
    lista_numeros = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    print("Rsultado en el proceso: ")
    p1 = multiprocessing.Process(target=calculo_raices, args=(lista_numeros,))

    p1.start()

    p1.join()

    print("Resultado en el main: ")
    print("Las raices de las lista son: {}".format(lista_raices))
    print("La suma de las raices de la lista es: {}".format(suma_total))

    print("\nProceso 1 esta vivo: {}".format(p1.is_alive()))

    print(
        "\nEs necesario llamar a la función en el main si se quiere obtener los resultados ya que el main y el proceso no comparten memoria y los cambios no se guardan: ")
    print("Resultados función: ")
    calculo_raices(lista_numeros)
    print("Resultado en el main: ")
    print("Las raices de las lista son: {} ".format(lista_raices))
    print("La suma de las raices de la lista es: {} ".format(suma_total))
