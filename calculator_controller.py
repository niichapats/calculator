from calculator_model import CalculatorModel
from calculator_view import CalculatorView


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)

    def number_operator_handler(self, event):
        text = str(self.view.display['text']) + event.widget['text']
        text_to_calculate = self.view.display['text']
        if text[-1] == '=':
            result = self.model.calculate_result(text_to_calculate)
            self.view.display.config(text=result)
            self.view.history.config(text=f'History : {self.model.show_history()}')
        elif text[-1] == 'R':
            self.view.display.config(text='')
        elif text[-1] == 'L':
            result = self.model.delete_last(text_to_calculate)
            self.view.display.config(text=result)
        else:
            self.view.display.config(text=text)

    def function_handler(self, event):
        text = str(self.view.display['text'])
        new_text = self.view.selected_function.get()
        selected_math_function = self.view.selected_function.get()
        check_text = text[-1] if text else None
        if not text or check_text in ['*', '/', '+', '-', '^', '=']:
            new_text = text + selected_math_function + '('
        elif check_text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            new_text = selected_math_function + '(' + text + ')'
        elif check_text == 'd':
            new_text = text + '(' + selected_math_function + '('
        self.view.display.config(text=new_text)

    def run(self):
        self.view.run()


if __name__ == '__main__':
    calculator = CalculatorController()
    # calculator.get_history()
    calculator.run()
