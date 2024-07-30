def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False

#Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numero_a_buscar = 8

resultado = busqueda_binaria(lista_ordenada, numero_a_buscar)


if resultado:
    print(f"El número {numero_a_buscar} está en la lista.")
else:
    print(f"El número {numero_a_buscar} no está en la lista.")
