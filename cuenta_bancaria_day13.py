class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto

    def consultar_saldo(self):
        return self.saldo

#Ejemplos
cuenta = CuentaBancaria(100) 
print(f"Saldo inicial: {cuenta.consultar_saldo()}")  

cuenta.depositar(50)
print(f"Saldo después de depositar 50: {cuenta.consultar_saldo()}")  

cuenta.depositar(30)
print(f"Saldo después de depositar 30: {cuenta.consultar_saldo()}")  
