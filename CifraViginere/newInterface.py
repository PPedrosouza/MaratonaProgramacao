from tkinter import *
import sys

janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.button()
        self.textbox()
        self.label()
        janela.mainloop()

    def tela(self):
        self.janela.title("Cifra de Vigenère")
        self.janela.geometry("600x400+200+200")
        self.janela.minsize(400, 200)
        self.janela.maxsize(800, 600)
        self.janela.configure(background='#ae3743')

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee')
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def button(self, key, message):
        
        self.bt_confirma = Button(self.frame_1, text="Confirmar", command = textCryptography(key, message))
        self.bt_confirma.place(relx=0.45, rely=0.45,
                               relheight=0.15, relwidth=0.15)

        self.bt_confirma2 = Button(self.frame_2, text="Confirmar", command = textDescryptography(key, message))
        self.bt_confirma2.place(relx=0.45, rely=0.25,
                                relheight=0.15, relwidth=0.15)

    def label(self):
        self.lbl_msg = Label(self.frame_1, text="Mensagem")
        self.lbl_msg.place(relx=0.01, rely=0.25, relheight=0.12, relwidth=0.13)
        self.lbl_key = Label(self.frame_1, text="Chave")
        self.lbl_key.place(relx=0.01, rely=0.1, relheight=0.12, relwidth=0.13)
        self.lbl_msgcripto = Label(self.frame_1, text="Criptografia")
        self.lbl_msgcripto.place(relx=0.01, rely=0.80,
                                 relheight=0.12, relwidth=0.13)

        self.lbl_key2 = Label(self.frame_2, text="Chave")
        self.lbl_key2.place(relx=0.01, rely=0.1, relheight=0.12, relwidth=0.13)
        self.lbl_msg_descript = Label(self.frame_2, text="Descriptografada")
        self.lbl_msg_descript.place(relx=0.4, rely=0.65,
                                    relheight=0.12, relwidth=0.25)

    def textbox(self):
        self.txt_key = Text(self.frame_1)
        self.txt_key.place(relx=0.15, rely=0.1, relheight=0.12, relwidth=0.85)
        self.txt_msg = Text(self.frame_1)
        self.txt_msg.place(relx=0.15, rely=0.25, relheight=0.12, relwidth=0.85)
        self.txt_msg_cripto = Text(self.frame_1, state="disabled")
        self.txt_msg_cripto.place(relx=0.15, rely=0.80,
                                  relheight=0.12, relwidth=0.85)

        self.txt_key2 = Text(self.frame_2)
        self.txt_key2.place(relx=0.15, rely=0.1, relheight=0.12, relwidth=0.85)
        self.txt_msg_descript = Text(self.frame_2, state="disabled")
        self.txt_msg_descript.place(relx=0.01, rely=0.8,
                                    relheight=0.12, relwidth=0.99)
        
        button(self.txt_key, self.txt_msg)

    def textCryptography(key, message):
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chave = ''  
        encriptar = ''

        mensagem = message.replace(' ', '').upper()	# Transforma as mensagens em maiusculo #
        chave_original = key.replace(' ', '').upper()	# Transforma a chave em maiusculo #

        if len(mensagem)>len(chave_original):	#
            for i in range(int(len(mensagem)/len(chave_original))):		##Dividindo para encaixar a chave dentro do texto ##
                chave += chave_original								
            chave += chave_original[:len(mensagem)%len(chave_original)]	
        elif len(mensagem)<len(chave_original):	
            chave = chave_original[:len(mensagem)]	# atribui o tamanho da mensagem para a chave original#
        elif len(mensagem)==len(chave_original):
            chave = chave_original	# se for igual, atribui a chave com a chave original#
        else:
            print ('Ocorreu um erro inesperado. Finalizando a execução...')
            sys.exit(1)

        for i in range(len(mensagem)):
            x = alfabeto.find(mensagem[i])	# armazena a posicao do caracter da letra da mensagem
            y = alfabeto.find(chave[i])	# armazena a posicao do caracter da letra da chave
            soma = x+y	# calcula a soma das posicoes
            modulo = soma%len(alfabeto)	# calcula o modulo da soma (matriz)
            encriptar += alfabeto[modulo]	

        # adicionar à parte do resultado
        
    def textDescryptography(key, message):
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chave = ''  
        encriptar = ''
        desencriptar = ''

        for i in range(len(encriptar)):
            x = alfabeto.find(encriptar[i])	# armazena a posicao do caracter da letra da mensagem
            y = alfabeto.find(chave[i])	# armazena a posicao do caracter da letra da chave
            resto = x-y	# calcula a soma das posicoes
            modulo = resto%len(alfabeto)	# calcula o modulo da soma (matriz)
            desencriptar += alfabeto[modulo]
        
        # adicionar à parte do resultado

Application()
