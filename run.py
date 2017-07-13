#!/usr/bin/python3

import curses
from Modules.Banco import Banco
import time
import sys



class Chat:

    def __init__(self):
        self.tela = curses.initscr()


    def select_message(self):
        try:
            self.tela = curses.initscr()
            message = Banco()
            buscar_mensagem = message.filter()
            self.tela.clear()
            for t in buscar_mensagem:
                self.tela.addstr(("[%s] %s : %s \n")%(t["hora"], str(t["name"]),t["message"]))
        except KeyboardInterrupt as e:
            sys.exit()



    def add_message(self,nome):
        try:
            self.tela.addstr(40,1,"Mensagem: ")
            input = self.tela.getstr(40, 11)
            self.tela.clear()
            message = Banco()
            message.add_message(name=nome, message=str(input))

        except KeyboardInterrupt as e:
            sys.exit()


if __name__ == '__main__':
    nome = input("Digite o seu nome: ")
    iniciar = Chat()
    while True:
        iniciar.select_message()
        iniciar.add_message(nome)