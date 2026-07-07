class calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a/b

calc = calculator()
print(calc.add(10,3))  # Output: 13
print(calc.multiply(10,3))  # Output: 30
print(calc.divide(10,3))  # Output: 3.333333333333
print(calc.divide(10,0))  # Output: Error: Division by zero

