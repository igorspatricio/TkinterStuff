class Cobra:
    def __init__(self, tamanho):
        self.corpo = [[0,0],[10,0],[20,0]]
        self.comprimento = len(self.corpo)
        self.tamanhoCorpo = tamanho
        self.direcao = [10, 0]
        self.color = "red"
        self.velocidade = 2
        self.viva = True

        self.moveu = True


    def addCorpo(self):
        print("ola")
        ult_posicao = len(self.corpo) - 1
        x, y = 0, 1
        novo = [self.corpo[ult_posicao][x] + self.direcao[x], self.corpo[ult_posicao][y] + self.direcao[y]]
        self.corpo.append(novo)
    def verifica_comida(self, x, y):
        ult_posicao = len(self.corpo) - 1
        return self.corpo[ult_posicao][0] == x and self.corpo[ult_posicao][1] == y




    def mover(self, WIDTH, HEIGHT):
        self.corpo.pop(0)
        ult_posicao= len(self.corpo)-1
        x, y = 0,1
        novo = [self.corpo[ult_posicao][x] + self.direcao[x], self.corpo[ult_posicao][y] + self.direcao[y]]
        if(novo[0] > WIDTH):
            novo[0] = 0
        elif (novo[0] < 0):
            novo[0] = WIDTH
        if(novo[1] > HEIGHT):
            novo[1] = 0
        elif(novo[1] < 0):
            novo[1] = HEIGHT
        for i in self.corpo:
            if(novo[0] == i[0] and novo[1] == i[1]):
                self.viva = False
        self.corpo.append(novo)
        self.moveu = True

    def get_viva(self):
        return self.viva




    def getCoords(self, parte):
        return [self.corpo[parte][0], self.corpo[parte][1], self.corpo[parte][0] + self.tamanhoCorpo,
                self.corpo[parte][1] + self.tamanhoCorpo]

    def nova_direcao(self, event):
        if(self.moveu):
            if(event.keysym == "Left" and self.direcao[0] == 0):
                self.direcao = [-10, 0]
                self.moveu = False
            elif(event.keysym == "Right" and self.direcao[0] == 0):
                self.direcao = [10, 0]
                self.moveu = False
            elif(event.keysym == "Up" and self.direcao[1] == 0):
                self.direcao = [0, -10]
                self.moveu = False
            elif(event.keysym == "Down" and self.direcao[1] == 0):
                self.direcao = [0, 10]
                self.moveu = False
