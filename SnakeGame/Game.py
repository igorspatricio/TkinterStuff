from tkinter import *

from Cobra import *
from Comida import *

WIDTH = 800
HEIGHT = 500
TAMANHO = 10

if __name__ == '__main__':
    root = Tk()
    cobrinha = Cobra(10)
    comida = Comida(10, WIDTH, HEIGHT)

    canva = Canvas(width=WIDTH, height=HEIGHT,  bg = "green")

    root.bind('<Left>', cobrinha.nova_direcao)
    root.bind('<Up>', cobrinha.nova_direcao)
    root.bind('<Right>', cobrinha.nova_direcao)
    root.bind('<Down>', cobrinha.nova_direcao)


    canva.pack()

    mover = True

    while(cobrinha.get_viva()):
        canva.after(20)

        for i in range(len(cobrinha.corpo)):
            canva.create_rectangle(cobrinha.getCoords(i), fill="red", outline="red")

        canva.create_rectangle(comida.getCoords(), fill='white', outline='white')

        x,y = comida.get_posicao()
        if(cobrinha.verifica_comida(x,y)):
            comida.nova_posicao()
            cobrinha.addCorpo()

        if(mover):
            cobrinha.mover(WIDTH, HEIGHT)
        mover = not(mover)

        canva.update()
        canva.delete('all')

        root.mainloop()

