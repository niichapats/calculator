import tkinter as tk
from tkinter import ttk
from keypad import Keypad


class CalculatorView(tk.Tk):
    def __init__(self, controller):
        """
        Contructor
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
        # if text_history is not None and text_history.strip():  # Check if text_history is not None or empty
        #     self.history = tk.Label(self, text=f'History\n{text_history}', bg='gray10', fg='lightpink', font=('monospace', 15), anchor=tk.W)
        #     self.history.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        # else:
        #     # Handle the case when text_history is None or empty
        self.history = tk.Label(self, text='History', bg='Black', fg='Salmon', font=('monospace', 15), anchor=tk.W)
        self.history.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.history_listbox = tk.Listbox(self, bg='gray10', fg='Lightsalmon', font=('monospace', 15), height=3, selectmode=tk.SINGLE)
        self.history_listbox.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.display = tk.Label(self, text='', bg='Black', fg='Light goldenrod', font=('monospace', 30), anchor=tk.E)
        self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.input_button = tk.Button(self, text='Recall Input', command=self.controller.recall_input)
        self.input_button.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.result_button = tk.Button(self, text='Recall Result', command=self.controller.recall_result)
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
        # self.history.bind("<Button-1>", self.controller.history_click_handler)

        # self.history_listbox.bind('<ButtonRelease-1>', self.history_click_handler)

    def clear_default_text(self, event):
        # Clear the default text when the user clicks on the combobox
        self.selected_function.set("")

    def selected_history(self):
        selected_history = self.history_listbox.get(tk.ANCHOR)
        return selected_history


    # def update_history_listbox(self, history_entries):
    #     # Clear and update the history Listbox
    #     self.history_listbox.delete(0, tk.END)
    #     for entry in history_entries:
    #         self.history_listbox.insert(tk.END, entry)
    #
    # def history_click_handler(self, event):
    #     # Get the selected index from the Listbox
    #     selected_index = self.history_listbox.curselection()
    #
    #     if selected_index:
    #         # Get the selected history entry
    #         selected_entry = self.history_listbox.get(selected_index)
    #
    #         # Determine whether it's an input or result
    #         if "=" in selected_entry:
    #             # Display the entire entry (input + result)
    #             self.display.config(text=selected_entry)
    #         else:
    #             # Display the input only
    #             self.display.config(text=selected_entry)


    def run(self):
        self.mainloop()



