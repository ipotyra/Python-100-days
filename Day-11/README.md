# Day 11 — The Blackjack Capstone Project

## 📌 Topics Covered
- Day 11 goals: what we will build by the end of the day
- Blackjack program requirements and game rules
- Hint 4 & 5 solution walkthrough
- Hint 6-8 solution walkthrough
- Hint 9 solution walkthrough: refactoring and calling `calculate_score()`
- Hint 10-12 solution walkthrough
- Hint 13 solution walkthrough
- A solid foundation goes a long way

## 🎯 Key Concepts

### Game Rules
- Simulate a simplified game of Blackjack against a computer dealer.
- Player and dealer are each dealt 2 cards from an infinite deck (cards can repeat).
- Card values: number cards = face value, J/Q/K = 10, Ace = 11 or 1 (whichever keeps the hand from busting).
- Player can choose to draw more cards ("hit") or stop ("stand").
- The dealer keeps hitting until their score is 17 or higher.
- Whoever gets closest to 21 without going over wins; going over 21 is a "bust".
- A 2-card 21 is a "Blackjack" and beats a regular 21.

### Refactoring with `calculate_score()`
- Extracting the score-calculation logic into its own function avoids repeating code for both player and dealer.
- Handles special cases: Blackjack (21 with exactly 2 cards) and Ace value adjustment (11 → 1 when busting).

## 🃏 Final Project — Blackjack

A command-line Blackjack game that:
1. Prints an ASCII art logo
2. Deals 2 random cards each to the player and the computer dealer
3. Calculates each hand's score, handling Aces and Blackjack as special cases
4. Lets the player choose to "hit" or "stand" in a loop
5. Runs the dealer's turn automatically once the player stands
6. Compares final scores and declares a winner, loser, or draw
7. Asks if the player wants to play again

## 🛠️ Skills Practiced
- Structuring a larger, multi-step program using functions
- Working with lists (the hand of cards) and `random.choice()`
- Looping with `while` for repeated player actions
- Conditional logic for scoring edge cases (Ace, Blackjack, bust)
- Refactoring repeated logic into a reusable function

---
*Part of the 100 Days of Code — Python Bootcamp*
