class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def show_history(self):
        return self.history

# Пример использования
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(2, 3))
    print(calc.multiply(4, 5))
    print("История:", calc.show_history())
