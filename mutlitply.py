class multiplication:
    def multiply(self, a, b):
        return a * b
    
if __name__ == "__main__":
    mul = multiplication()
    num1 = int(input())
    num2 = int(input())
    result = mul.multiply(num1, num2)
    