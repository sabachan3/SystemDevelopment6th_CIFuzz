class InvalidInputException(Exception):
    pass

class Calculator:
    MAX_VALUE = 1000000
    MIN_VALUE = -1000000

    def _validate_input(self, *values):
        for value in values:
            if value > self.MAX_VALUE or value < self.MIN_VALUE:
                raise InvalidInputException(
                    f"Input value {value} is outside the valid range "
                    f"[{self.MIN_VALUE}, {self.MAX_VALUE}]"
                )

    def add(self, a, b):
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        self._validate_input(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

