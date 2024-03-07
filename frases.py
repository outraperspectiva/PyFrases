
import random
from tkinter import messagebox, Tk, Label, Button

frases = ["  sim  ", "  não  ", "talvez"]

def responder():
    resposta_label = Label(text=frases[random.randrange(3)])
    resposta_label.grid(row=2, column=1, columnspan=2)
    botao_sorteio["text"] ="próxima resposta"

janela = Tk()
janela.title("Gerador de Frases")
janela.config(padx=100, pady=10)
frase_label = Label(text="faça sua pergunta")
frase_label.grid(row=1, column=0)

botao_sorteio = Button(text="Responder pergunta", width=36, command=responder)
botao_sorteio.grid(row=4, column=1, columnspan=2)

janela.mainloop()