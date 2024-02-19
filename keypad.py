"""Use for creating a keypad"""

import tkinter as tk
from tkinter import ttk, Frame


class Keypad(Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__()
        self.parent = parent
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:

        key_list = []
        row = len(self.keynames) // columns
        options = {'sticky': tk.NSEW}
        for i in self.keynames:
            button = tk.Button(self, text=i)
            key_list.append(button)
        index = 0
        for row in range(row):
            for column in range(columns):
                key_list[index].grid(row=row, column=column, **options)
                index += 1

        for i in range(row+1):
            self.rowconfigure(i, weight=4)
        for i in range(columns):
            self.columnconfigure(i, weight=4)

    def bind(self, sequence=None, function=None, add=None):
        """Bind an event handler to an event sequence."""
        for item in self.winfo_children():
            item.bind(sequence, function, add)

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """

        for item in self.winfo_children():
            item.configure(cnf, **kwargs)
