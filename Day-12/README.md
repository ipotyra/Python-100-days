# Day 12 — Scope & the Number Guessing Game

## 📌 Topics Covered
- Day 12 goals: what we will build by the end of the day
- Namespaces: Local vs. Global Scope
- Does Python have block scope?
- Prime Number Checker (exercise)
- How to modify a global variable from inside a function
- Python constants and global scope
- Scope Quiz
- Introducing the final project: The Number Guessing Game

## 🎯 Key Concepts

### Namespaces: Local vs. Global Scope
- A **local** variable is defined inside a function and only exists within that function's namespace.
- A **global** variable is defined at the top level of a script and is accessible (read-only) from anywhere, including inside functions.
- If a local variable has the same name as a global one, the local variable takes priority *inside that function* — this is called **shadowing**.

### Does Python Have Block Scope?
- Unlike languages such as Java or C, Python does **not** have block scope — `if`, `for`, and `while` blocks do not create a new scope.
- A variable created inside an `if`/`for`/`while` block is still accessible outside the block, as long as it's within the same function or module.
- Python only creates a new scope for **functions** (and classes, lambdas).

### Modifying a Global Variable
- By default, a function can *read* a global variable but assigning to a variable of the same name inside a function creates a new **local** variable instead of modifying the global one.
- The `global` keyword tells Python to use the global variable instead of creating a local one:

```python
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies: {enemies}")

increase_enemies()  # enemies: 2
print(enemies)      # 2
```

### Python Constants and Global Scope
- Python has no true constant type — by convention, constants are written in `ALL_CAPS` to signal "do not reassign this".
- Constants are typically declared as global variables at the top of a module, outside any function.

## 🔢 Final Project — Number Guessing Game

A command-line game that:
1. Prints an ASCII art logo
2. Picks a random number between 1 and 100
3. Asks the player to guess the number, tracking remaining lives per difficulty level
4. Gives "too high" / "too low" feedback after each guess using `global` to update the guess count/lives
5. Ends the game with a win or loss message, and offers to play again

## 🛠️ Skills Practiced
- Reasoning about local vs. global scope when reading and writing code
- Using the `global` keyword deliberately, and understanding why it's often avoided
- Structuring a small game around functions that share state via global variables
- Working with `random.randint()` for number generation

---
*Part of the 100 Days of Code — Python Bootcamp*
