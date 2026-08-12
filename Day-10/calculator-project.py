def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}
print("\n".join(operation.keys()))
choose = operation[input("what operation would you like to perform? ")]
print(choose(float(input("what is the first number? ")), float(input("what is the second number? "))))