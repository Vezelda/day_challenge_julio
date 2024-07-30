##Ordenamiento por Selección

def selection_sort(lista):
    longitud = len(lista)
    for indice_actual in range(longitud):
        indice_minimo = indice_actual
        for indice_siguiente in range(indice_actual + 1, longitud):
            if lista[indice_siguiente] < lista[indice_minimo]:
                indice_minimo = indice_siguiente
        lista[indice_actual], lista[indice_minimo] = lista[indice_minimo], lista[indice_actual] #Intercambia el elemento mínimo con el primer elemento no ordenado
    return lista

#ejemplo
lista = [5, 2, 3, 8, 12, 9, 1, 5]
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)