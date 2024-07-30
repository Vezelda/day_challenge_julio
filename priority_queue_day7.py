class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)
        self.queue.sort()  #Ordena la lista después de insertar

    def remove(self):
        if not self.is_empty():
            return self.queue.pop(0)  #Eliminamos y retornamos el elemento con mayor prioridad (menor valor)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return ' '.join(map(str, self.queue))

#Creamos la cola de prioridad y luego insertamos 5 elementos
pq = PriorityQueue()
elementos = [20, 15, 10, 5, 30]

print("Insertando elementos:")
for elem in elementos:
    pq.insert(elem)
    print(f"Insertado {elem}, cola actual: {pq}")

# Eliminamos elementos de la cola de prioridad
print("\nEliminando elementos:")
while not pq.is_empty():
    eliminado = pq.remove()
    print(f"Eliminado {eliminado}, cola actual: {pq}")
