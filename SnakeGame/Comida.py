import random


class Comida:
    def __init__(self, tamanho, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self.tamanho = tamanho
        x = random.randint(0, WIDTH/self.tamanho)
        y = random.randint(0, HEIGHT/self.tamanho)
        self.posicao = [x*self.tamanho, y*self.tamanho]

    def getCoords(self):
        return [self.posicao[0], self.posicao[1], self.posicao[0]+self.tamanho,   self.posicao[1]+self.tamanho]

    def nova_posicao(self):
        x = random.randint(0, self.width / self.tamanho)
        y = random.randint(0, self.height / self.tamanho)
        self.posicao = [x * self.tamanho, y * self.tamanho]

    def get_posicao(self):
        return self.posicao