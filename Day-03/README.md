# Day 03 - Control Flow and Logical Operators

## What I learned

### if, elif, and else
`if`, `elif`, and `else` let a program make decisions and run different code 
depending on whether a condition is `True` or `False`.

- **`if`** checks a condition. If it's `True`, the code block inside runs.
- **`elif`** ("else if") checks another condition, but only if the previous 
  `if` was `False`. You can have as many `elif` blocks as needed.
- **`else`** runs if none of the previous conditions were `True`. It doesn't 
  check a condition itself — it's the fallback.

Example:
```python
age = 20

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
```
Python checks each condition **in order**, top to bottom, and runs the first 
block whose condition is `True`. If none match, it runs the `else` block.

### Comparison operators
Used to compare values inside conditions:
- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

### Logical operators
Used to combine multiple conditions:
- **`and`** — both conditions must be `True`
- **`or`** — at least one condition must be `True`
- **`not`** — reverses a condition (`True` becomes `False`, and vice versa)

Example:
```python
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    print("Good day for a walk!")
```

### Indentation matters
Python uses indentation (spaces) to define which code belongs inside an 
`if`/`elif`/`else` block — there are no curly braces `{}` like in other 
languages. Consistent indentation is required, or the code will raise an error.

## Exercises
- BMI (Body Mass Index) calculator using if/elif/else

## Resources
- 
