from calculator_model import CalculatorModel
from calculator_view import CalculatorView
import tkinter as tk


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)

    def number_operator_handler(self, event):
        """
        Handle when the user entered number or operator.
        :param event:
        :return:
        """
        text = str(self.view.display['text']) + event.widget['text']
        text_to_calculate = self.view.display['text']
        result, success = self.model.calculate_result(text_to_calculate)
        if text[-1] == '=':
            self.evaluate_expression()
            if success is True:
                self.show_history()
        elif text[-1] == 'R':
            self.view.display.config(text='', fg='Light goldenrod')
        elif text[-1] == 'L':
            result = self.model.delete_last(text_to_calculate)
            self.view.display.config(text=result, fg='Light goldenrod')
        else:
            self.view.display.config(text=text, fg='Light goldenrod')

    def function_handler(self, event):
        """
        Handle when the user chose the math function in the combobox.
        :param event:
        :return:
        """
        text = str(self.view.display['text'])
        new_text = self.view.selected_function.get()
        selected_math_function = self.view.selected_function.get()
        check_text = text[-1] if text else None
        if not text or check_text in ['*', '/', '+', '-', '^', '=']:  # handle when the last element on the display is an operator
            new_text = text + selected_math_function + '('
        elif check_text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:  # handle when the last element on the display is a number
            new_text = selected_math_function + '(' + text + ')'
        elif check_text == 'd':  # handle when the last element on the display is 'mod'
            new_text = text + '(' + selected_math_function + '('
        self.view.display.config(text=new_text, fg='Light goldenrod')

    def evaluate_expression(self):
        """
        Check if it is possible to calculate the result.
        If possible, display it on the screen.
        Otherwise, indicate an error by changing the inout
        on the display to red and emitting an alert sound.
        :return:
        """
        text = str(self.view.display['text'])
        result, success = self.model.calculate_result(text)

        if success:
            self.view.display.config(text=result, fg='Light goldenrod')
        else:
            self.view.display.config(fg='red')  # Change color for invalid expression
            self.model.play_sound()

    def recall_input(self):
        """
        Handle when the user wants to recall the input.
        Recall the input from the selected history to show on the display.
        :return:
        """
        selected_history = self.view.selected_history()
        selected_input = None
        for item in self.model.history:
            if f"{item['input']} = {item['result']}" == selected_history:
                selected_input = item['input']
        self.view.display.config(text=selected_input)

    def recall_result(self):
        """
        Handle when the user wants to recall the result.
        Recall the result from the selected history to show on the display.
        :return:
        """
        selected_history = self.view.selected_history()
        selected_result = None
        for item in self.model.history:
            if f"{item['input']} = {item['result']}" == selected_history:
                selected_result = item['result']
        self.view.display.config(text=selected_result)

    def show_history(self):
        """
        Retrieve history from the model and display it.
        :return:
        """
        history = self.model.format_history()
        self.view.history_listbox.insert(tk.END, history[-1])

    def run(self):
        """
        Run the program by running CalculatorView
        :return:
        """
        self.view.run()
