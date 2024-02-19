from math import *
from playsound import playsound


class CalculatorModel:
    def __init__(self):
        self.history = []

    def calculate_result(self, text):
        """
        Calculate the result from the equation(text)
        :param text:
        :return Result , State(Success or not):
        """
        try:
            # Attempt to evaluate the expression
            if 'mod' in text:
                text = text.replace('mod', '%')
            if 'ln' in text:
                text = text.replace('ln', 'log')
            result = eval(text)
            new_history = {'input': text, 'result': result}
            self.history.append(new_history)
            return result, True  # Indicate success
        except Exception as e:
            return str(e), False  # Return the error message and indicate failure

    @staticmethod
    def delete_last(text):
        """
        Delete the last element that the user entered
        :param text:
        :return new_text:
        """
        text = str(text)
        if len(text) == 1:
            return ''
        new_text = text[:-1]
        for math_function in ['exp', 'ln', 'log10', 'log2', 'sqrt']:
            if text.endswith(math_function):
                selected_math_function = math_function
                new_text = text.replace(selected_math_function, '')
        return new_text

    def format_history(self):
        """
        Get formatted history for display on the screen
        :return:
        """
        format_history = []
        for item in self.history:
            format_history.append(f"{item['input']} = {item['result']}")
        return format_history

    @staticmethod
    def play_sound():
        """
        Play the sound (error sound)
        :return:
        """
        playsound('sound.wav')
