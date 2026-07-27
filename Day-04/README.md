# Day 04 - Randomisation and Python Lists

## What I learned
- Using the `random` module for randomisation
- Creating and working with Python lists
- List indexing and basic list operations

## Exercises
- Banker roulette exercise
- Rock, Paper, Scissors game

## Resources
- 

## How randomness is created
Python's `random` module doesn't generate true randomness — it uses a pseudo-random
number generator called the **Mersenne Twister** algorithm. This means the numbers
only *look* random, but are actually calculated from a starting value called a **seed**
(usually based on the system clock if you don't set one manually). With the same seed,
you'd always get the same sequence of "random" results — which is why it's called
pseudo-random rather than truly random.

## Variable naming discussion
My last variable was `random_friends`:
\`\`\`python
random_friends = random.choice(friends)
\`\`\`
This name is misleading because it's plural (`friends`) but actually stores a single
value — only one friend is chosen. A clearer name would be singular, like `chosen_friend`
or `random_friend`, to reflect that it holds one item, not a list.
