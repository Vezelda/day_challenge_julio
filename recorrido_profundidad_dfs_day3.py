#Creamos el grafo usando un diccionario de listas
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

#Función principal
def dfs(grafo, nodo, visitados):
    visitados.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

#Iniciamos el conjunto de nodos visitados y llamamos a DFS
visitados = set()
dfs(grafo, 0, visitados)
