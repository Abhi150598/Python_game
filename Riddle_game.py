#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def get_random_riddle():
    riddles = {
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?(4 letters)": "echo",
        "I come from a mine and get surrounded by wood always. Everyone uses me. What am I?(6 letters)": "pencil",
        "I have branches, but no fruit, trunk or leaves. What am I?(4 letters)": "bank",
        "What can travel around the world while staying in a corner?(5 letters)": "stamp",
        "The more of this there is, the less you see. What is it?(8 letters)": "darkness"
    }
    riddle, answer = random.choice(list(riddles.items()))
    return riddle, answer

def play_riddle_game():
    riddle, answer = get_random_riddle()
    attempts_remaining = 3
    guessed_letters = set()

    print("Welcome to the Riddle Guessing Game!")
    print("Solve the riddle by guessing the correct word.(use lowercase only)")
    print(f"Riddle: {riddle}")

    while attempts_remaining > 0:
        guess = input("Enter your guess: ").lower()

        if guess == answer:
            print(f"Congratulations! You guessed the word: {answer}")
            break
        else:
            attempts_remaining -= 1
            print(f"Wrong guess! You have {attempts_remaining} attempts remaining.")

        if attempts_remaining == 0:
            print(f"\nGame Over! The correct answer was: {answer}")

if __name__ == "__main__":
    play_riddle_game()

