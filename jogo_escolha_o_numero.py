import random

class Jogo:                   # Classe que inicia o jogo 
    def __init__(self):
        self.valor_maximo = 100
        self.valor_minimo = 1
        self.num_aletorio = 0
        self.tentar = True



    def num_alet(self):       # Método que escolhe o número de forma aleatória  
        self.num_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

    def chute(self):          # Método que avalia o "chute" do usuário e orienta o mesmo até ao número esolhido 
        self.num_alet()
        self.pedir_cht()


        while self.tentar == True:
            if int(self.cht) > (self.num_aleatorio):
                print('O número aleatório está abaixo da sua escolha')
                self.pedir_cht()
            elif int(self.cht) < (self.num_aleatorio):
                print('O número aleatório está acima da sua escolha.')
                self.pedir_cht()
            if int(self.cht) == (self.num_aleatorio):
                self.tentar = False
                print('Parabéns você ACERTOU!!!!.')


    def pedir_cht(self):    # Método que pede ao usuário a sua escolha, caso o número escolhido seja maior que 100 é enviado um alerta
        self.cht = (input("Qual a sua escolha? "))
        if int(self.cht) > 100:
            print("Sua escolha deve está entre 1 e 100.")





tent = Jogo()
tent.chute()
