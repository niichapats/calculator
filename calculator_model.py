class CalculatorModel:
    def __init__(self):
        self.history = []

    def calculate_result(self, text):
        if 'mod' in text:
            text = text.replace('mod', '%')
        result = eval(text)
        new_history = str(text) + ' = ' + str(result)
        self.history.append(new_history)
        print(self.history)
        return result

    @staticmethod
    def delete_last(text):
        result = text[:-1]
        for math_function in ['exp', 'ln', 'log10', 'log2', 'sqrt']:
            if text.endswith(math_function):
                selected_math_function = math_function
                result = text.replace(selected_math_function, '')
        return result

    def show_history(self):
        text_history = ''
        for history in self.history:
            text_history += history + '  |  '
        print(text_history)
        return text_history


if __name__ == '__main__':
    model = CalculatorModel()
    model.show_history()
