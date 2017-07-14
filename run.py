#!/usr/bin/python3

import curses
from Modules.Banco import Banco
import time
import sys
import threading
from select import select





class Chat:

    def __init__(self):
        self.tela = curses.initscr()

    def select_message(self):
        try:
            while True:
                message = Banco()
                buscar_mensagem = message.filter()
                self.tela.clear()

                for t in buscar_mensagem:
                    self.tela.addstr(("[%s] %s : %s \n")%(t["hora"], t["name"],str(t["message"])))
        except Exception as e:
            curses.endwin()
            sys.exit()



    def add_message(self, input):
        try:
            self.tela.addstr(40, 1, "Mensagem: ")
            input = self.tela.getstr(40, 11).decode(encoding="utf-8")
            message = Banco()
            message.add_message(name=nome, message=str(input))


        except Exception as e:
            curses.endwin()
            sys.exit()





if __name__ == '__main__':
    nome = input("Digite o seu nome: ")
    iniciar = Chat()
    t = threading.Thread(target=iniciar.select_message)
    t.start()
    while True:
        iniciar.add_message(nome)


