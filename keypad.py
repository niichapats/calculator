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
        options = {'sticky': tk.NSEW}  # make button fill the grid cell
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

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        pass

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return Keypad(self)

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """

        for item in self.winfo_children():
            item.configure(cnf, **kwargs)

if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
