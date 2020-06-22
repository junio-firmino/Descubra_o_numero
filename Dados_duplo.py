import random

class Dados():
    def __init__(self):
        self.dados_min = 1          # Estabelecemos o valor mínimo do dado
        self.dados_max = 6          # Estabelecemos o valor máximo do dado
        self.num_aletorio = 0       # Estabelecemos que essa variável comece do zero
        self.num_aletorio_2 = 0     # Estabelecemos que essa variável comece do zero

    def interface (self):           # Chamada inicial do programa
        print("Jogo dos dados.")    

    def dados_aleat(self):
        self.interface()
        self.num_aletorio = random.randint(self.dados_min,self.dados_max)       # Escolha dos numeros aleatórios (dado 1) 
        self.num_aletorio_2 = random.randint(self.dados_min,self.dados_max)     # Escolha dos numeros aleatórios (dado 2)
        soma = int(self.num_aletorio) + int(self.num_aletorio_2)                # Soma dos valores escolhidos para ajudar os jogadores

        print('o numero escolhido do dado 1 é: ' + str(self.num_aletorio))
        print('o numero escolhido do dado 2 é: ' + str(self.num_aletorio_2))
        print ('Ande ' + str(soma) + ' casas.')

        self.final()


    def final(self):                # Método final 
        print('Este é o nosso protótipo de dados para jogos de tabuleiro.')


jogo = Dados()
jogo.dados_aleat()
