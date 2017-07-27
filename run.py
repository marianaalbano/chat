#!/usr/bin/python3

import curses
from Modules.Banco import Banco
import sys


class Chat:

    def __init__(self):
        self.tela = curses.initscr()

    def select_message(self):
        try:

            message = Banco()
            buscar_mensagem = message.filter()
            self.tela.clear()
            for t in buscar_mensagem:
                self.tela.addstr(("[%s] %s : %s \n")%(t["hora"], str(t["name"]), t["message"]))
            self.tela.refresh()
        except KeyboardInterrupt as e:
            curses.endwin()
            sys.exit()

    def add_message(self, input):
        try:
            self.tela.addstr("Mensagem: ")
            input = self.tela.getstr().decode(encoding="utf-8")
            self.tela.clear()
            message = Banco()
            message.add_message(name=nome, message=str(input))

        except KeyboardInterrupt as e:
            curses.endwin()
            sys.exit()


if __name__ == '__main__':
    try:
        nome = input("Digite o seu nome: ")
        iniciar = Chat()
        while True:
            iniciar.select_message()
            iniciar.add_message(nome)
    except KeyboardInterrupt as e:
        curses.endwin()
        sys.exit()
