import tkinter as tk
from tkinter import ttk
from keypad import Keypad


class CalculatorView(tk.Tk):
    def __init__(self, controller):
        """
        Constructor
        :param controller:
        """
        super().__init__()
        self.controller = controller
        self.title('Caculator')
        self.number_frame = Keypad(self, list('789456123 0.'), 3)
        self.operator_frame1 = Keypad(self, ['mod', '*', '/', '+', '-', '^', '='], 1)
        self.operator_frame2 = Keypad(self, ['CLR', '(', ')', 'DEL'], 4)
        self.math_function = ['exp', 'ln', 'log10', 'log2', 'sqrt']
        self.default_text = 'Math Function'
        self.selected_function = tk.StringVar()
        self.selected_function.set(self.default_text)
        self.init_component()

    def init_component(self):
        """
        Initialize the CalculatorView instance.
        :return:
        """
        self.history = tk.Label(self, text='History', bg='Black', fg='Salmon', font=('monospace', 15), anchor=tk.W)
        self.history.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.history_listbox = tk.Listbox(self, bg='gray10', fg='LightSalmon', font=('monospace', 15), height=3, selectmode=tk.SINGLE)
        self.history_listbox.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.display = tk.Label(self, text='', bg='Black', fg='Light goldenrod', font=('monospace', 30), anchor=tk.E)
        self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.input_button = tk.Button(self, fg='PaleGreen4', text='Recall Input', command=self.controller.recall_input)
        self.input_button.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.result_button = tk.Button(self, fg='Cyan4', text='Recall Result', command=self.controller.recall_result)
        self.result_button.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        math_function_combobox = ttk.Combobox(self, textvariable=self.selected_function, values=self.math_function, state="readonly")
        math_function_combobox.pack(side=tk.BOTTOM, anchor=tk.S, pady=10, expand=True, fill=tk.BOTH)

        self.operator_frame2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.number_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.operator_frame1.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.number_frame.bind('<Button>', self.controller.number_operator_handler)
        self.operator_frame1.bind('<Button>', self.controller.number_operator_handler)
        self.operator_frame2.bind('<Button>', self.controller.number_operator_handler)
        math_function_combobox.bind('<<ComboboxSelected>>', self.clear_default_text)
        math_function_combobox.bind('<<ComboboxSelected>>', self.controller.function_handler)

    def clear_default_text(self, event):
        """
        Clear the default text when the user clicks on the combobox
        :param event:
        :return:
        """
        self.selected_function.set("")

    def selected_history(self):
        """
        Get what the user selected from history_listbox
        :return selected_history:
        """
        selected_history = self.history_listbox.get(tk.ANCHOR)
        return selected_history

    def run(self):
        """
        Run the program (CalculatorView)
        :return:
        """
        self.mainloop()



