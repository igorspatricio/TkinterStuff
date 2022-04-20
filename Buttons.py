from tkinter import *
def click():
    nome.set(entrada.get())

root = Tk()
nome = StringVar()
label = Label(textvariable=nome)
entrada = Entry(root)

botao = Button(root, text="Escreva seu nome!", command=click)


botao.grid(row=1, column=0)
entrada.grid(row=0, column=0)
label.grid(row=2, column=0)
root.mainloop()
