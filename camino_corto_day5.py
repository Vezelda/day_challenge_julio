import heapq

#utilice dijkstra ya que habia usado antes A*
def dijkstra(graph, start, goal):
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances [start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == goal:
            path = []
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            path.insert(0, start)
            return distances[goal], path

        #Procesar los nodos vecinos
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return float('infinity'), []

#Representar el grafo como un diccionario
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
}


start_node = 'A'
goal_node = 'E'
cost, path = dijkstra(graph, start_node, goal_node)
print(f"El camino más corto de {start_node} a {goal_node} es {path} con un costo total de {cost}")
