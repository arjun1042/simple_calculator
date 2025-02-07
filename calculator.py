class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Simple Calculator!")
    print("1. Add")
    print("2. Subtract")
    
    choice = input("Choose an operation (1/2): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = calc.add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = calc.subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    else:
        print("Invalid choice!")