from collections import deque

#Creamos el grafo usando un diccionario de listas
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

#Función BFS
def bfs(grafo, nodo_inicial):
    visitados = set()
    cola = deque([nodo_inicial])
    
    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo)
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

#iniciamos el programa
bfs(grafo, 0)
