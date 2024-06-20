class Equation:
        def __init__(self, variable_count, variable_names, function):
            self.variable_count = variable_count
            self.variable_names = variable_names
            self.function = function

        def evaluate(self, variable_values):
            return self.function(variable_values)