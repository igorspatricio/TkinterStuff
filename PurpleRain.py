import random
from tkinter import *


if __name__ == '__main__':
    janelaRaiz = Tk()
    canva = Canvas(width=500, height=250, background='cyan')
    canva.pack()
    chuva = []
    velocidade2 = []
    for i in range(200):
        x = random.randint(0, 500)
        y = random.randint(0, 250)
        chuva.append(canva.create_line(x, y, x, y+10, fill="purple"))
        velocidade2.append(random.randint(1,3))

    global cond
    cond = True
    def click():
        global cond
        cond=False

    botao = Button(janelaRaiz, text="Fechar", bg="red", command=lambda:click())
    botao.pack()


    while(cond):
        for i in chuva:

            velocidade = velocidade2[i-1]
            xy = canva.coords(i)

            if(xy[3] >= 249):
                velocidade2[i - 1] = random.randint(1,5)
                x = random.randint(0, 500)
                y = 0
                xy = [x, y, x, y+10]

            xy[1] += velocidade
            xy[3]+= velocidade
            canva.coords(i, xy)
        janelaRaiz.update()





    # janelaRaiz.mainloop()
