from tkinter import *

class Application:
    def _init_(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados para criptografar/descriptografar")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.key = Label(self.segundoContainer,text="Chave Criptográfica", font=self.fontePadrao)
        self.key.pack(side=LEFT)

        self.key = Entry(self.segundoContainer)
        self.key["width"] = 30
        self.key["font"] = self.fontePadrao
        self.key.pack(side=LEFT)

        self.text = Label(self.terceiroContainer, text="Mensagem", font=self.fontePadrao)
        self.text.pack(side=LEFT)

        self.text = Entry(self.terceiroContainer)
        self.text["width"] = 30
        self.text["font"] = self.fontePadrao
        self.text["show"] = "*"
        self.text.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.cryptoKey
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # função que irá pegar a chave e criptogramar e descriptografar
    def cryptoKey(self):
        key = self.key.get()
        text = self.text.get()


root = Tk()
Application(root)
root.mainloop()