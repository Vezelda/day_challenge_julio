class Pila:
    def __init__(self):
        self.pila = []

    def juntar(self, elemento):
        self.pila.append(elemento)

    def desjuntar(self):
        if not self.vaciado():
            return self.pila.pop()
        else:
            return None

    def vaciado(self):
        return len(self.pila) == 0

    def __str__(self):
        return ' '.join(map(str, self.pila))

# Crear una pila y luego insertamos 5 elementos
pila = Pila()
elementos = [1, 2, 3, 4, 5]

print("Metemos el elemento en la pila:")
for elem in elementos:
    pila.juntar(elem)
    print(f"Insertando {elem}, a la pila actual: {pila}")

# Eliminamos elementos de la pila
print("\nBorramos elementos de la pila:")
while not pila.vaciado():
    eliminado = pila.desjuntar()
    print(f"Se elimino {eliminado}, la pila actual es: {pila}")
