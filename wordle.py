import enchant
import pandas as pd
import random

checker = enchant.Dict('en_US')
df = pd.read_csv('5_letter_words.csv')
words = df['word'].tolist()

word = random.choice(words)
print(word)

while True:
    userGuess = input("Please enter a 5 letter word: ")
    if len(userGuess) != 5:
        userGuess = input("Input needs to be 5 characters!")
    
    if checker.check(userGuess):
        if userGuess.lower == word:
            print("Correct!")
            break
        else:
            count = 0
            for i in userGuess:
                if i in word and userGuess.index(i) == word.index(i):
                    print(f'\u001b[32m{i}\u001b[0m', end="")
                elif i in word and userGuess.index(i) != word.index(i):
                    print(f'\u001b[33m{i}\u001b[0m', end="")
                else:
                    print(f'\u001b[31m{i}\u001b[0m', end="")
            print()

    else:
        print("Not a word!")



