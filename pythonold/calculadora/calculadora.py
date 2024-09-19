class calculadora():
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.resultado = 0

    def iniciar(self):
        try:
            self.numero1 = int(input('-Digite um numero: >>>'))
            self.opcao = str(input('-Digite a operação: >>>'))
            self.numero2 = int(input('-Digite um numero: >>>'))
        except:
            print('ERRO')

        if self.opcao == '+':
            self.somar()
        elif self.opcao == '-':
            self.subtrair()
        elif self.opcao == '*':
            self.multiplicar()
        elif self.opcao == '/':
            self.divisao()


    def somar(self):
       self.resultado = self.numero1 + self.numero2
       print(self.resultado)

    def subtrair(self):
       self.resultado = self.numero1 - self.numero2
       print(self.resultado)

    def multiplicar(self):
       self.resultado = self.numero1 * self.numero2
       print(self.resultado)

    def divisao(self):
       self.resultado = self.numero1 / self.numero2
       print(self.resultado)



calculadora = calculadora()

calculadora.iniciar()