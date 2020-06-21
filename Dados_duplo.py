import random

class Dados():
    def __init__(self):
        self.dados_min = 1
        self.dados_max = 6
        self.num_aletorio = 0
        self.num_aletorio_2 = 0

    def interface (self):
        print("Jogo dos dados.")

    def dados_aleat(self):
        self.interface()
        self.num_aletorio = random.randint(self.dados_min,self.dados_max)
        self.num_aletorio_2 = random.randint(self.dados_min,self.dados_max)

        soma = int(self.num_aletorio) + int(self.num_aletorio_2)

        print('o numero escolhido do dado 1 é: ' + str(self.num_aletorio))
        print('o numero escolhido do dado 2 é: ' + str(self.num_aletorio_2))
        print ('Ande ' + str(soma) + ' casas.')

        self.final()


    def final(self):
        print('Este é o nosso protótipo de dados para jogos de tabuleiro.')


jogo = Dados()
jogo.dados_aleat()
