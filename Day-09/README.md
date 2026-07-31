# Day 9 - Dictionaries, Nesting and the Secret Auction

## 🎯 Goals

- Understand what dictionaries are in Python and how to use them
- Learn how to nest lists inside dictionaries and vice versa
- Practice iterating over dictionaries with `.items()`
- Apply all of this in a real program: **Grading Program**

## 📚 Concepts covered

### Dictionaries

Data structures that store `key: value` pairs, unlike lists which use numeric indexes.

```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
```

**Main operations:**
- Access a value: `dictionary["key"]`
- Add/update: `dictionary["new_key"] = value`
- Loop through: `for key, value in dictionary.items():`
- Empty dictionary: `{}`

### Nesting

Dictionaries can contain lists, and lists can contain dictionaries — allowing for more complex and realistic data structures.

```python
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
```

## 💻 Exercise: Grading Program

A program that converts student scores (`student_scores`) into grades (`student_grades`) using a dictionary and a `for` loop.

**Grading criteria:**
| Score | Grade |
|-------|-------|
| 91-100 | Outstanding |
| 81-90 | Exceeds Expectations |
| 71-80 | Acceptable |
| ≤ 70 | Fail |

➡️ File: [`grading_program.py`](./grading_program.py)

## 🔜 Next steps

- [ ] Nesting Lists and Dictionaries (lesson 69)
- [ ] Quiz 7: Python Dictionaries
- [ ] Secret Auction Program (day project)

## 🧠 Learnings / difficulties

> Space to note what was tricky, what clicked, and questions to revisit later.

-
-
