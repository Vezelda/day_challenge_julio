class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def describir(self):
        return f"Motor tipo: {self.tipo}"

class Auto:
    def __init__(self, tipo_motor):
        self.motor = Motor(tipo_motor)

    def describir_motor(self):
        return self.motor.describir()

#Ejemplo
mi_auto = Auto("V8")
print(mi_auto.describir_motor())
