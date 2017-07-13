import curses
import curses.textpad
import os

class Layout:
    TITLE_ROWS = 1
    PROMPT_ROWS = 1

    def __init__(self):
        "Determine the terminal size, and size of each window"

        # Get terminal size
        self.rows, self.cols = Layout.terminal_size()

        # Calculate dimensions of each window
        self.title_rows         = Layout.TITLE_ROWS
        self.title_cols         = self.cols
        self.title_start_row    = 0
        self.title_start_col    = 0

        self.history_rows       = self.rows - Layout.TITLE_ROWS - Layout.PROMPT_ROWS
        self.history_cols       = self.cols
        self.history_start_row  = 1
        self.history_start_col  = 0

        self.prompt_rows        = Layout.PROMPT_ROWS
        self.prompt_cols        = self.cols
        self.prompt_start_row   = self.rows - 1
        self.prompt_start_col   = 0




class Prompt:
    def __init__(self, layout, screen):
        self.layout = layout
        self.screen = screen
        self.window = curses.newwin(1, 1, 1-1 , 0)
        self.window.keypad(1)
        self.window.addstr('> ')

    def getchar(self):
        "Get a single character from the user"
        return self.window.getch()

    def getstr(self):
        "Get an input string from the user"
        return self.window.getstr()

    def redraw(self):
        "Redraw the prompt window"
        self.window.refresh()

    def reset(self):
        "Reset the prompt to '> ' and redraw"
        self.window.clear()
        self.window.addstr('> ')
        self.redraw()


if __name__ == '__main__':
    t = Prompt()

