# Day 05 - Loops

## What I learned
- `for` loops and `while` loops
- Iterating over lists and ranges
- Using loops to repeat tasks and build patterns

## Exercises
- Password generator

## Resources
- 

## Handling invalid input
Currently, the password generator doesn't handle bad input well:
- If the user types a letter instead of a number, `int()` crashes the program with
  a `ValueError`.
- If the user enters a negative number, no error occurs, but `range(0, -3)` produces
  an empty sequence — so that part of the password is silently skipped, which can
  confuse the user.

**Possible fix:** wrap the input in a `try/except` block and check for negative values:
\`\`\`python
try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    if nr_letters < 0:
        print("Please enter a positive number.")
except ValueError:
    print("Please enter a valid number, not text.")
\`\`\`

## Copying the password to clipboard instead of printing it
For better security, the password could be copied directly to the user's clipboard
instead of being printed to the screen — this avoids exposing it if someone is
watching the terminal or if the output gets logged.

This can be done with the \`pyperclip\` library:
\`\`\`bash
pip install pyperclip
\`\`\`
\`\`\`python
import pyperclip

pyperclip.copy(password)
print("Password copied to clipboard!")
\`\`\`
