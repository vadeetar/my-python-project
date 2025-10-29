def greeting():
    return "Привет! Это проект Тарасова Вадима"

def calculate(a, b):
    return a + b

def main():
    print(greeting())
    result = calculate(5, 3)
    print(f"Результат вычисления: {result}")

if __name__ == "__main__":
    main()
