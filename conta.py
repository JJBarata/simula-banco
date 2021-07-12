class Conta:
    # Construtor
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print('Conta {} de {}, possui saldo de {} Reais e limite de {} Reais'.format(numero, titular, saldo, limite))

    # Métodos

    # Saldo líquido
    @property
    def saldo(self):
        return self.__saldo

    # Salto total (saldo líquido + limite)
    @property
    def saldo_com_limite(self):
        return self.__saldo + self.__limite

    @property
    def limite(self):
        return self.__limite

    # Conta recebe novo limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= self.saldo_com_limite

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print('Saque efetuado!')
        else:
            print('Saldo insuficiente!')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        self.extrato()

    @property
    def titular(self):
        return self.__titular

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

