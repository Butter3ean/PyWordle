import enchant
import pandas as pd
import random
import tkinter as tk

checker = enchant.Dict('en_US')
df = pd.read_csv('5_letter_words.csv')
words = df['word'].tolist()

word_entry = tk.StringVar()


def getWord():
    userEntry.get()

def wordle():
    while True:
        userGuess = getWord()
        if len(userGuess) != 5:
            userGuess = getWord()
        
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

window = tk.Tk()

label = tk.Label(text="Please Enter a Five Letter Word")
userEntry = tk.Entry(width=50)
submitBtn = tk.Button(text='Submit', command=wordle)
label.pack()
userEntry.pack()
submitBtn.pack()


word = random.choice(words)


print(word)

window.mainloop()




