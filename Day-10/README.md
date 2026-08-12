# Day 10 — Functions with Outputs (Return Values)

## 📌 Topics Covered
- What a `return` statement does and how it differs from `print()`
- Functions that take inputs *and* give back outputs
- Storing a function's return value in a variable for later use
- Using return values as inputs to other functions
- Docstrings for documenting what a function does
- `None` — what it means when a function has no `return`

## 🎯 Key Concepts

### `print()` vs `return`
- `print()` only displays something in the console — it does not give the program a value to work with afterward.
- `return` sends a value back to wherever the function was called, so it can be saved in a variable and reused.

```python
def add(n1, n2):
    return n1 + n2

result = add(3, 5)
print(result)  # 8
```

### Functions Can Return Any Data Type
A function can return a number, string, boolean, list, dictionary, or even another function.

### No `return`? → `None`
If a function doesn't explicitly return anything, Python returns `None` by default.

## 🧮 Final Project — Calculator

A command-line calculator that:
1. Prints an ASCII art logo
2. Asks the user for two numbers
3. Shows a menu of operations: `+`, `-`, `*`, `/`
4. Performs the chosen calculation using functions that `return` results
5. Asks if the user wants to continue calculating with the last result, or start a new calculation

### Example Structure
```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or 'n' to start new. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
```

## 🛠️ Skills Practiced
- Writing reusable functions with return values
- Using a dictionary to map symbols to functions (mini "switch statement")
- Recursion (calling `calculator()` inside itself to restart)
- Combining functions to build a complete, interactive program


---
*Part of the 100 Days of Code — Python Bootcamp*