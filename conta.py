class Conta:
    # Definindo a função construtora
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print('Conta {} de {}, possui saldo de {} Reais e limite de {} Reais'.format(numero, titular, saldo, limite))

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

